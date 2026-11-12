"""
Send endpoints must not be retried automatically when the caller gave no Idempotency-Key.

A 5xx (for example a gateway timeout) can reach the client after the API already sent the email.
Without a key the API cannot tell a resend from a new send, so an automatic retry delivers the
email twice. With a key the API returns the original message, so retrying stays safe.
"""

import typing

import httpx
import pytest

from agentmail import AgentMail, AsyncAgentMail
from agentmail.core.api_error import ApiError
from agentmail.environment import AgentMailEnvironment

ENV = AgentMailEnvironment(http="http://agentmail.test", websockets="ws://agentmail.test")
SENT = {"message_id": "msg-1", "thread_id": "thr-1"}


@pytest.fixture(autouse=True)
def no_backoff(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr("agentmail.core.http_client._retry_timeout", lambda response, retries: 0)


class Recorder:
    """In-memory transport: answers with `statuses` in order, then 200, and records every request."""

    def __init__(self, *statuses: int) -> None:
        self.statuses = list(statuses)
        self.requests: typing.List[httpx.Request] = []

    def __call__(self, request: httpx.Request) -> httpx.Response:
        self.requests.append(request)
        if self.statuses:
            return httpx.Response(self.statuses.pop(0), json={"name": "Error", "message": "upstream timed out"})
        if request.method == "GET":
            return httpx.Response(200, json={"count": 0, "inboxes": []})
        return httpx.Response(200, json=SENT)


def client(recorder: Recorder) -> AgentMail:
    return AgentMail(
        api_key="test", environment=ENV, httpx_client=httpx.Client(transport=httpx.MockTransport(recorder))
    )


SENDS: typing.Dict[str, typing.Callable[..., typing.Any]] = {
    "messages.send": lambda c, **kw: c.inboxes.messages.send("inbox-1", to="a@example.com", text="hi", **kw),
    "messages.reply": lambda c, **kw: c.inboxes.messages.reply("inbox-1", "msg-0", text="hi", **kw),
    "messages.reply_all": lambda c, **kw: c.inboxes.messages.reply_all("inbox-1", "msg-0", text="hi", **kw),
    "messages.forward": lambda c, **kw: c.inboxes.messages.forward("inbox-1", "msg-0", to="a@example.com", **kw),
    "drafts.send": lambda c, **kw: c.inboxes.drafts.send("inbox-1", "draft-1", **kw),
}


@pytest.mark.parametrize("status", [500, 502, 503, 504, 408, 409])
@pytest.mark.parametrize("name", list(SENDS))
def test_send_without_key_is_sent_once_after_ambiguous_error(name: str, status: int) -> None:
    recorder = Recorder(status)
    with pytest.raises(ApiError) as exc_info:
        SENDS[name](client(recorder))
    assert exc_info.value.status_code == status
    assert len(recorder.requests) == 1


@pytest.mark.parametrize("name", list(SENDS))
def test_send_with_key_is_still_retried_with_the_same_key(name: str) -> None:
    recorder = Recorder(502)
    result = SENDS[name](client(recorder), idempotency_key="order-4821")
    assert result.message_id == "msg-1"
    assert [r.headers["Idempotency-Key"] for r in recorder.requests] == ["order-4821", "order-4821"]


def test_send_with_key_in_additional_headers_is_still_retried() -> None:
    recorder = Recorder(503)
    SENDS["messages.send"](client(recorder), request_options={"additional_headers": {"idempotency-key": "k-1"}})
    assert len(recorder.requests) == 2


def test_send_without_key_is_still_retried_on_429() -> None:
    recorder = Recorder(429)
    result = SENDS["messages.send"](client(recorder))
    assert result.message_id == "msg-1"
    assert len(recorder.requests) == 2


def test_reads_are_still_retried_on_5xx() -> None:
    recorder = Recorder(503)
    client(recorder).inboxes.list()
    assert [r.method for r in recorder.requests] == ["GET", "GET"]


async def test_async_send_without_key_is_sent_once_after_5xx() -> None:
    recorder = Recorder(502)
    async_client = AsyncAgentMail(
        api_key="test", environment=ENV, httpx_client=httpx.AsyncClient(transport=httpx.MockTransport(recorder))
    )
    with pytest.raises(ApiError):
        await async_client.inboxes.messages.send("inbox-1", to="a@example.com", text="hi")
    assert len(recorder.requests) == 1
