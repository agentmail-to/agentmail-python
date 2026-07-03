# Tests for the hand-written Idempotency-Key auto-mint patch. Pinned in
# .fernignore so Fern regeneration cannot clobber it.

import uuid
from typing import List

import httpx
import pytest

from agentmail.core.http_client import HttpClient
from agentmail.core.request_options import RequestOptions


def _is_valid_uuid4(value: str) -> bool:
    try:
        parsed = uuid.UUID(value)
    except (ValueError, TypeError, AttributeError):
        return False
    return parsed.version == 4 and str(parsed) == value.lower()


def _make_client(handler: httpx.MockTransport) -> HttpClient:
    return HttpClient(
        httpx_client=httpx.Client(transport=handler),
        base_timeout=lambda: None,
        base_headers=lambda: {},
        base_url=lambda: "https://api.agentmail.to/v0",
    )


def _capture_transport(captured: List[httpx.Request], status_codes: List[int]) -> httpx.MockTransport:
    """MockTransport that records each request and returns the next status code."""
    calls = {"i": 0}

    def handle(request: httpx.Request) -> httpx.Response:
        captured.append(request)
        idx = min(calls["i"], len(status_codes) - 1)
        calls["i"] += 1
        return httpx.Response(status_codes[idx], json={})

    return httpx.MockTransport(handle)


def test_send_path_mints_uuid4_idempotency_key() -> None:
    captured: List[httpx.Request] = []
    client = _make_client(_capture_transport(captured, [200]))

    client.request(path="messages/send", method="POST", json={"to": "a@b.com"}, request_options=None)

    assert len(captured) == 1
    key = captured[0].headers.get("Idempotency-Key")
    assert key is not None
    assert _is_valid_uuid4(key)


def test_caller_supplied_key_is_preserved() -> None:
    captured: List[httpx.Request] = []
    client = _make_client(_capture_transport(captured, [200]))

    options: RequestOptions = {"additional_headers": {"Idempotency-Key": "caller-key-123"}}
    client.request(path="messages/send", method="POST", json={"to": "a@b.com"}, request_options=options)

    assert len(captured) == 1
    assert captured[0].headers.get("Idempotency-Key") == "caller-key-123"


def test_retry_reuses_identical_key() -> None:
    captured: List[httpx.Request] = []
    # 503 once, then 200 -> the client should retry and both attempts share the key.
    client = _make_client(_capture_transport(captured, [503, 200]))

    client.request(
        path="messages/send",
        method="POST",
        json={"to": "a@b.com"},
        request_options={"max_retries": 2},
    )

    assert len(captured) == 2
    keys = [r.headers.get("Idempotency-Key") for r in captured]
    assert keys[0] is not None
    assert _is_valid_uuid4(keys[0])
    assert keys[0] == keys[1]


def test_non_send_post_is_not_injected() -> None:
    captured: List[httpx.Request] = []
    client = _make_client(_capture_transport(captured, [200]))

    client.request(path="inboxes", method="POST", json={"username": "x"}, request_options=None)

    assert len(captured) == 1
    assert "Idempotency-Key" not in captured[0].headers


def test_two_calls_mint_different_keys() -> None:
    captured: List[httpx.Request] = []
    client = _make_client(_capture_transport(captured, [200]))

    client.request(path="messages/send", method="POST", json={"to": "a@b.com"}, request_options=None)
    client.request(path="messages/send", method="POST", json={"to": "c@d.com"}, request_options=None)

    assert len(captured) == 2
    key1 = captured[0].headers.get("Idempotency-Key")
    key2 = captured[1].headers.get("Idempotency-Key")
    assert key1 is not None and key2 is not None
    assert key1 != key2


def test_create_draft_path_is_not_injected() -> None:
    captured: List[httpx.Request] = []
    client = _make_client(_capture_transport(captured, [200]))

    # /messages/{id}/draft-reply is a create-draft endpoint, NOT a send.
    client.request(path="messages/msg_123/draft-reply", method="POST", json={}, request_options=None)

    assert len(captured) == 1
    assert "Idempotency-Key" not in captured[0].headers


@pytest.mark.parametrize(
    "path",
    [
        "messages/send",
        "messages/msg_1/reply",
        "messages/msg_1/reply-all",
        "messages/msg_1/forward",
        "drafts/dft_1/send",
    ],
)
def test_all_send_paths_are_injected(path: str) -> None:
    captured: List[httpx.Request] = []
    client = _make_client(_capture_transport(captured, [200]))

    client.request(path=path, method="POST", json={}, request_options=None)

    assert "Idempotency-Key" in captured[0].headers, f"expected injection for {path}"


@pytest.mark.parametrize(
    "path",
    [
        "messages/msg_1/draft-reply",
        "messages/msg_1/draft-reply-all",
        "messages/msg_1/draft-forward",
    ],
)
def test_create_draft_paths_are_not_injected(path: str) -> None:
    captured: List[httpx.Request] = []
    client = _make_client(_capture_transport(captured, [200]))

    client.request(path=path, method="POST", json={}, request_options=None)

    assert "Idempotency-Key" not in captured[0].headers, f"unexpected injection for {path}"


def test_send_path_with_query_string_is_injected() -> None:
    captured: List[httpx.Request] = []
    client = _make_client(_capture_transport(captured, [200]))

    client.request(path="messages/send?foo=bar", method="POST", json={}, request_options=None)

    assert "Idempotency-Key" in captured[0].headers


def test_get_on_send_path_is_not_injected() -> None:
    captured: List[httpx.Request] = []
    client = _make_client(_capture_transport(captured, [200]))

    client.request(path="messages/send", method="GET", request_options=None)

    assert "Idempotency-Key" not in captured[0].headers
