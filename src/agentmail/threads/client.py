# This file was auto-generated by Fern from our API Definition.

from ..core.client_wrapper import SyncClientWrapper
from ..inboxes.types.inbox_id import InboxId
import typing
from ..types.received import Received
from ..types.sent import Sent
from ..types.limit import Limit
from ..types.last_key import LastKey
from ..core.request_options import RequestOptions
from .types.list_threads_response import ListThreadsResponse
from ..core.jsonable_encoder import jsonable_encoder
from ..core.pydantic_utilities import parse_obj_as
from ..errors.not_found_error import NotFoundError
from ..types.error_response import ErrorResponse
from json.decoder import JSONDecodeError
from ..core.api_error import ApiError
from .types.thread_id import ThreadId
from .types.thread import Thread
from ..core.client_wrapper import AsyncClientWrapper


class ThreadsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list(
        self,
        inbox_id: InboxId,
        *,
        received: typing.Optional[Received] = None,
        sent: typing.Optional[Sent] = None,
        limit: typing.Optional[Limit] = None,
        last_key: typing.Optional[LastKey] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListThreadsResponse:
        """
        List threads in inbox. If neither or both `received` and `sent` query parameters are set, all threads are returned.

        Parameters
        ----------
        inbox_id : InboxId

        received : typing.Optional[Received]

        sent : typing.Optional[Sent]

        limit : typing.Optional[Limit]

        last_key : typing.Optional[LastKey]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListThreadsResponse

        Examples
        --------
        from agentmail import AgentMail

        client = AgentMail(
            api_key="YOUR_API_KEY",
        )
        client.threads.list(
            inbox_id="yourinbox@agentmail.to",
            limit=10,
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v0/inboxes/{jsonable_encoder(inbox_id)}/threads",
            method="GET",
            params={
                "received": received,
                "sent": sent,
                "limit": limit,
                "last_key": last_key,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    ListThreadsResponse,
                    parse_obj_as(
                        type_=ListThreadsResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def get(
        self, inbox_id: InboxId, thread_id: ThreadId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Thread:
        """
        Parameters
        ----------
        inbox_id : InboxId

        thread_id : ThreadId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Thread

        Examples
        --------
        from agentmail import AgentMail

        client = AgentMail(
            api_key="YOUR_API_KEY",
        )
        client.threads.get(
            inbox_id="yourinbox@agentmail.to",
            thread_id="thread_123",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v0/inboxes/{jsonable_encoder(inbox_id)}/threads/{jsonable_encoder(thread_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    Thread,
                    parse_obj_as(
                        type_=Thread,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncThreadsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list(
        self,
        inbox_id: InboxId,
        *,
        received: typing.Optional[Received] = None,
        sent: typing.Optional[Sent] = None,
        limit: typing.Optional[Limit] = None,
        last_key: typing.Optional[LastKey] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListThreadsResponse:
        """
        List threads in inbox. If neither or both `received` and `sent` query parameters are set, all threads are returned.

        Parameters
        ----------
        inbox_id : InboxId

        received : typing.Optional[Received]

        sent : typing.Optional[Sent]

        limit : typing.Optional[Limit]

        last_key : typing.Optional[LastKey]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListThreadsResponse

        Examples
        --------
        import asyncio

        from agentmail import AsyncAgentMail

        client = AsyncAgentMail(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.threads.list(
                inbox_id="yourinbox@agentmail.to",
                limit=10,
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v0/inboxes/{jsonable_encoder(inbox_id)}/threads",
            method="GET",
            params={
                "received": received,
                "sent": sent,
                "limit": limit,
                "last_key": last_key,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    ListThreadsResponse,
                    parse_obj_as(
                        type_=ListThreadsResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def get(
        self, inbox_id: InboxId, thread_id: ThreadId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Thread:
        """
        Parameters
        ----------
        inbox_id : InboxId

        thread_id : ThreadId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Thread

        Examples
        --------
        import asyncio

        from agentmail import AsyncAgentMail

        client = AsyncAgentMail(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.threads.get(
                inbox_id="yourinbox@agentmail.to",
                thread_id="thread_123",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v0/inboxes/{jsonable_encoder(inbox_id)}/threads/{jsonable_encoder(thread_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    Thread,
                    parse_obj_as(
                        type_=Thread,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)
