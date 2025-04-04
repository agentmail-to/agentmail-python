# This file was auto-generated by Fern from our API Definition.

import typing
from ..core.client_wrapper import SyncClientWrapper
from ..types.limit import Limit
from ..types.last_key import LastKey
from ..core.request_options import RequestOptions
from .types.list_webhooks_response import ListWebhooksResponse
from ..core.pydantic_utilities import parse_obj_as
from json.decoder import JSONDecodeError
from ..core.api_error import ApiError
from .types.webhook_id import WebhookId
from .types.webhook import Webhook
from ..core.jsonable_encoder import jsonable_encoder
from ..errors.not_found_error import NotFoundError
from ..types.error_response import ErrorResponse
from .types.url import Url
from .types.events import Events
from .types.inboxes import Inboxes
from ..errors.validation_error import ValidationError
from ..types.validation_error_response import ValidationErrorResponse
from ..core.client_wrapper import AsyncClientWrapper

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class WebhooksClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list(
        self,
        *,
        limit: typing.Optional[Limit] = None,
        last_key: typing.Optional[LastKey] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListWebhooksResponse:
        """
        Parameters
        ----------
        limit : typing.Optional[Limit]

        last_key : typing.Optional[LastKey]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListWebhooksResponse

        Examples
        --------
        from agentmail import AgentMail

        client = AgentMail(
            api_key="YOUR_API_KEY",
        )
        client.webhooks.list()
        """
        _response = self._client_wrapper.httpx_client.request(
            "v0/webhooks",
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
                    ListWebhooksResponse,
                    parse_obj_as(
                        type_=ListWebhooksResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def get(
        self,
        webhook_id: WebhookId,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Webhook:
        """
        Parameters
        ----------
        webhook_id : WebhookId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Webhook

        Examples
        --------
        from agentmail import AgentMail

        client = AgentMail(
            api_key="YOUR_API_KEY",
        )
        client.webhooks.get(
            webhook_id="webhook_id",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v0/webhooks/{jsonable_encoder(webhook_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    Webhook,
                    parse_obj_as(
                        type_=Webhook,  # type: ignore
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
        url: Url,
        events: typing.Optional[Events] = OMIT,
        inboxes: typing.Optional[Inboxes] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Webhook:
        """
        Parameters
        ----------
        url : Url

        events : typing.Optional[Events]

        inboxes : typing.Optional[Inboxes]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Webhook

        Examples
        --------
        from agentmail import AgentMail

        client = AgentMail(
            api_key="YOUR_API_KEY",
        )
        client.webhooks.create(
            url="url",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "v0/webhooks",
            method="POST",
            json={
                "url": url,
                "events": events,
                "inboxes": inboxes,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    Webhook,
                    parse_obj_as(
                        type_=Webhook,  # type: ignore
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

    def delete(
        self,
        webhook_id: WebhookId,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        webhook_id : WebhookId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from agentmail import AgentMail

        client = AgentMail(
            api_key="YOUR_API_KEY",
        )
        client.webhooks.delete(
            webhook_id="webhook_id",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v0/webhooks/{jsonable_encoder(webhook_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return
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


class AsyncWebhooksClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list(
        self,
        *,
        limit: typing.Optional[Limit] = None,
        last_key: typing.Optional[LastKey] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListWebhooksResponse:
        """
        Parameters
        ----------
        limit : typing.Optional[Limit]

        last_key : typing.Optional[LastKey]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListWebhooksResponse

        Examples
        --------
        import asyncio

        from agentmail import AsyncAgentMail

        client = AsyncAgentMail(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.webhooks.list()


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v0/webhooks",
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
                    ListWebhooksResponse,
                    parse_obj_as(
                        type_=ListWebhooksResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def get(
        self,
        webhook_id: WebhookId,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Webhook:
        """
        Parameters
        ----------
        webhook_id : WebhookId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Webhook

        Examples
        --------
        import asyncio

        from agentmail import AsyncAgentMail

        client = AsyncAgentMail(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.webhooks.get(
                webhook_id="webhook_id",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v0/webhooks/{jsonable_encoder(webhook_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    Webhook,
                    parse_obj_as(
                        type_=Webhook,  # type: ignore
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
        url: Url,
        events: typing.Optional[Events] = OMIT,
        inboxes: typing.Optional[Inboxes] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Webhook:
        """
        Parameters
        ----------
        url : Url

        events : typing.Optional[Events]

        inboxes : typing.Optional[Inboxes]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Webhook

        Examples
        --------
        import asyncio

        from agentmail import AsyncAgentMail

        client = AsyncAgentMail(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.webhooks.create(
                url="url",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v0/webhooks",
            method="POST",
            json={
                "url": url,
                "events": events,
                "inboxes": inboxes,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    Webhook,
                    parse_obj_as(
                        type_=Webhook,  # type: ignore
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

    async def delete(
        self,
        webhook_id: WebhookId,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        webhook_id : WebhookId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from agentmail import AsyncAgentMail

        client = AsyncAgentMail(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.webhooks.delete(
                webhook_id="webhook_id",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v0/webhooks/{jsonable_encoder(webhook_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return
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
