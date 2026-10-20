from unittest.mock import patch

import pytest
from websockets.datastructures import Headers
from websockets.exceptions import InvalidStatus, InvalidStatusCode  # type: ignore[attr-defined]
from websockets.http11 import Response

from agentmail import AgentMail, AsyncAgentMail
from agentmail.core.api_error import ApiError


def rejection(status, legacy):
    if legacy:
        return InvalidStatusCode(status, Headers())
    return InvalidStatus(Response(status, "Rejected", Headers()))


@pytest.mark.parametrize("status", [401, 403, 503])
@pytest.mark.parametrize("legacy", [False, True])
def test_sync_websocket_rejection_is_api_error(status, legacy):
    client = AgentMail(api_key="test-key")
    with patch("agentmail.websockets.client.websockets_sync_client.connect", side_effect=rejection(status, legacy)):
        with pytest.raises(ApiError) as caught:
            with client.websockets.connect():
                pytest.fail("Rejected handshake must not yield a socket")
    assert caught.value.status_code == status
    expected = (
        "Websocket initialized with invalid credentials."
        if status == 401
        else "Unexpected error when initializing websocket connection."
    )
    assert caught.value.body == expected


@pytest.mark.parametrize("status", [401, 403, 503])
@pytest.mark.parametrize("legacy", [False, True])
async def test_async_websocket_rejection_is_api_error(status, legacy):
    client = AsyncAgentMail(api_key="test-key")
    with patch("agentmail.websockets.client.websockets_client_connect", side_effect=rejection(status, legacy)):
        with pytest.raises(ApiError) as caught:
            async with client.websockets.connect():
                pytest.fail("Rejected handshake must not yield a socket")
    assert caught.value.status_code == status
    expected = (
        "Websocket initialized with invalid credentials."
        if status == 401
        else "Unexpected error when initializing websocket connection."
    )
    assert caught.value.body == expected
