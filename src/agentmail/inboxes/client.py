# This file was auto-generated by Fern from our API Definition.

import typing
from ..core.client_wrapper import SyncClientWrapper
from ..types.limit import Limit
from ..types.last_key import LastKey
from ..core.request_options import RequestOptions
from .types.list_inboxes_response import ListInboxesResponse
from ..core.pydantic_utilities import parse_obj_as
from json.decoder import JSONDecodeError
from ..core.api_error import ApiError
from .types.inbox_id import InboxId
from .types.inbox import Inbox
from ..core.jsonable_encoder import jsonable_encoder
from ..errors.not_found_error import NotFoundError
from ..types.error_response import ErrorResponse
from .types.display_name import DisplayName
from ..errors.validation_error import ValidationError
from ..types.validation_error_response import ValidationErrorResponse
from ..core.client_wrapper import AsyncClientWrapper

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class InboxesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list(
        self,
        *,
        limit: typing.Optional[Limit] = None,
        last_key: typing.Optional[LastKey] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListInboxesResponse:
        """
        Parameters
        ----------
        limit : typing.Optional[Limit]

        last_key : typing.Optional[LastKey]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListInboxesResponse

        Examples
        --------
        from agentmail import AgentMail

        client = AgentMail(
            api_key="YOUR_API_KEY",
        )
        client.inboxes.list(
            limit=10,
            last_key="123e4567-e89b-12d3-a456-426614174000",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "v0/inboxes",
            method="GET",
            params={
                "limit": limit,
                "last_key": last_key,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    ListInboxesResponse,
                    parse_obj_as(
                        type_=ListInboxesResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def get(self, inbox_id: InboxId, *, request_options: typing.Optional[RequestOptions] = None) -> Inbox:
        """
        Parameters
        ----------
        inbox_id : InboxId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Inbox

        Examples
        --------
        from agentmail import AgentMail

        client = AgentMail(
            api_key="YOUR_API_KEY",
        )
        client.inboxes.get(
            inbox_id="yourinbox@agentmail.to",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v0/inboxes/{jsonable_encoder(inbox_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    Inbox,
                    parse_obj_as(
                        type_=Inbox,  # type: ignore
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

    def create(
        self,
        *,
        username: typing.Optional[str] = OMIT,
        domain: typing.Optional[str] = OMIT,
        display_name: typing.Optional[DisplayName] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Inbox:
        """
        Parameters
        ----------
        username : typing.Optional[str]
            Username of address. Randomly generated if not specified.

        domain : typing.Optional[str]
            Domain of address. Must be verified domain. Defaults to `agentmail.to`.

        display_name : typing.Optional[DisplayName]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Inbox

        Examples
        --------
        from agentmail import AgentMail

        client = AgentMail(
            api_key="YOUR_API_KEY",
        )
        client.inboxes.create(
            username="yourinbox",
            display_name="Your Inbox",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "v0/inboxes",
            method="POST",
            json={
                "username": username,
                "domain": domain,
                "display_name": display_name,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    Inbox,
                    parse_obj_as(
                        type_=Inbox,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            if _response.status_code == 400:
                raise ValidationError(
                    typing.cast(
                        ValidationErrorResponse,
                        parse_obj_as(
                            type_=ValidationErrorResponse,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncInboxesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list(
        self,
        *,
        limit: typing.Optional[Limit] = None,
        last_key: typing.Optional[LastKey] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListInboxesResponse:
        """
        Parameters
        ----------
        limit : typing.Optional[Limit]

        last_key : typing.Optional[LastKey]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListInboxesResponse

        Examples
        --------
        import asyncio

        from agentmail import AsyncAgentMail

        client = AsyncAgentMail(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.inboxes.list(
                limit=10,
                last_key="123e4567-e89b-12d3-a456-426614174000",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v0/inboxes",
            method="GET",
            params={
                "limit": limit,
                "last_key": last_key,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    ListInboxesResponse,
                    parse_obj_as(
                        type_=ListInboxesResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def get(self, inbox_id: InboxId, *, request_options: typing.Optional[RequestOptions] = None) -> Inbox:
        """
        Parameters
        ----------
        inbox_id : InboxId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Inbox

        Examples
        --------
        import asyncio

        from agentmail import AsyncAgentMail

        client = AsyncAgentMail(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.inboxes.get(
                inbox_id="yourinbox@agentmail.to",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v0/inboxes/{jsonable_encoder(inbox_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    Inbox,
                    parse_obj_as(
                        type_=Inbox,  # type: ignore
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

    async def create(
        self,
        *,
        username: typing.Optional[str] = OMIT,
        domain: typing.Optional[str] = OMIT,
        display_name: typing.Optional[DisplayName] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Inbox:
        """
        Parameters
        ----------
        username : typing.Optional[str]
            Username of address. Randomly generated if not specified.

        domain : typing.Optional[str]
            Domain of address. Must be verified domain. Defaults to `agentmail.to`.

        display_name : typing.Optional[DisplayName]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Inbox

        Examples
        --------
        import asyncio

        from agentmail import AsyncAgentMail

        client = AsyncAgentMail(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.inboxes.create(
                username="yourinbox",
                display_name="Your Inbox",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v0/inboxes",
            method="POST",
            json={
                "username": username,
                "domain": domain,
                "display_name": display_name,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    Inbox,
                    parse_obj_as(
                        type_=Inbox,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            if _response.status_code == 400:
                raise ValidationError(
                    typing.cast(
                        ValidationErrorResponse,
                        parse_obj_as(
                            type_=ValidationErrorResponse,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)
