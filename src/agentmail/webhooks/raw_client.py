# This file was auto-generated by Fern from our API Definition.

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import jsonable_encoder
from ..core.request_options import RequestOptions
from ..core.unchecked_base_model import construct_type
from ..errors.not_found_error import NotFoundError
from ..errors.validation_error import ValidationError
from ..types.error_response import ErrorResponse
from ..types.limit import Limit
from ..types.page_token import PageToken
from ..types.validation_error_response import ValidationErrorResponse
from .types.client_id import ClientId
from .types.event_types import EventTypes
from .types.inbox_ids import InboxIds
from .types.list_webhooks_response import ListWebhooksResponse
from .types.url import Url
from .types.webhook import Webhook
from .types.webhook_id import WebhookId

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class RawWebhooksClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list(
        self,
        *,
        limit: typing.Optional[Limit] = None,
        page_token: typing.Optional[PageToken] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ListWebhooksResponse]:
        """
        Parameters
        ----------
        limit : typing.Optional[Limit]

        page_token : typing.Optional[PageToken]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ListWebhooksResponse]
        """
        _response = self._client_wrapper.httpx_client.request(
            "v0/webhooks",
            base_url=self._client_wrapper.get_environment().http,
            method="GET",
            params={
                "limit": limit,
                "page_token": page_token,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListWebhooksResponse,
                    construct_type(
                        type_=ListWebhooksResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get(
        self, webhook_id: WebhookId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Webhook]:
        """
        Parameters
        ----------
        webhook_id : WebhookId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Webhook]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v0/webhooks/{jsonable_encoder(webhook_id)}",
            base_url=self._client_wrapper.get_environment().http,
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Webhook,
                    construct_type(
                        type_=Webhook,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        construct_type(
                            type_=ErrorResponse,  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def create(
        self,
        *,
        url: Url,
        event_types: EventTypes,
        inbox_ids: typing.Optional[InboxIds] = OMIT,
        client_id: typing.Optional[ClientId] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Webhook]:
        """
        Parameters
        ----------
        url : Url

        event_types : EventTypes

        inbox_ids : typing.Optional[InboxIds]

        client_id : typing.Optional[ClientId]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Webhook]
        """
        _response = self._client_wrapper.httpx_client.request(
            "v0/webhooks",
            base_url=self._client_wrapper.get_environment().http,
            method="POST",
            json={
                "url": url,
                "event_types": event_types,
                "inbox_ids": inbox_ids,
                "client_id": client_id,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Webhook,
                    construct_type(
                        type_=Webhook,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise ValidationError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ValidationErrorResponse,
                        construct_type(
                            type_=ValidationErrorResponse,  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def delete(
        self, webhook_id: WebhookId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        webhook_id : WebhookId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v0/webhooks/{jsonable_encoder(webhook_id)}",
            base_url=self._client_wrapper.get_environment().http,
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        construct_type(
                            type_=ErrorResponse,  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawWebhooksClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list(
        self,
        *,
        limit: typing.Optional[Limit] = None,
        page_token: typing.Optional[PageToken] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ListWebhooksResponse]:
        """
        Parameters
        ----------
        limit : typing.Optional[Limit]

        page_token : typing.Optional[PageToken]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ListWebhooksResponse]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v0/webhooks",
            base_url=self._client_wrapper.get_environment().http,
            method="GET",
            params={
                "limit": limit,
                "page_token": page_token,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListWebhooksResponse,
                    construct_type(
                        type_=ListWebhooksResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get(
        self, webhook_id: WebhookId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Webhook]:
        """
        Parameters
        ----------
        webhook_id : WebhookId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Webhook]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v0/webhooks/{jsonable_encoder(webhook_id)}",
            base_url=self._client_wrapper.get_environment().http,
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Webhook,
                    construct_type(
                        type_=Webhook,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        construct_type(
                            type_=ErrorResponse,  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def create(
        self,
        *,
        url: Url,
        event_types: EventTypes,
        inbox_ids: typing.Optional[InboxIds] = OMIT,
        client_id: typing.Optional[ClientId] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Webhook]:
        """
        Parameters
        ----------
        url : Url

        event_types : EventTypes

        inbox_ids : typing.Optional[InboxIds]

        client_id : typing.Optional[ClientId]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Webhook]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v0/webhooks",
            base_url=self._client_wrapper.get_environment().http,
            method="POST",
            json={
                "url": url,
                "event_types": event_types,
                "inbox_ids": inbox_ids,
                "client_id": client_id,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Webhook,
                    construct_type(
                        type_=Webhook,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise ValidationError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ValidationErrorResponse,
                        construct_type(
                            type_=ValidationErrorResponse,  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def delete(
        self, webhook_id: WebhookId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        webhook_id : WebhookId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v0/webhooks/{jsonable_encoder(webhook_id)}",
            base_url=self._client_wrapper.get_environment().http,
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        construct_type(
                            type_=ErrorResponse,  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
