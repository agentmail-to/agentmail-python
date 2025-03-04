# This file was auto-generated by Fern from our API Definition.

import typing
from ..core.client_wrapper import SyncClientWrapper
from ..inboxes.types.inbox_id import InboxId
from ..types.received import Received
from ..types.sent import Sent
from ..types.limit import Limit
from ..types.last_key import LastKey
from ..core.request_options import RequestOptions
from .types.list_messages_response import ListMessagesResponse
from ..core.jsonable_encoder import jsonable_encoder
from ..core.pydantic_utilities import parse_obj_as
from ..errors.not_found_error import NotFoundError
from ..types.error_response import ErrorResponse
from json.decoder import JSONDecodeError
from ..core.api_error import ApiError
from .types.message_id import MessageId
from .types.message import Message
from .types.attachment_id import AttachmentId
from .types.send_message_to import SendMessageTo
from .types.send_message_cc import SendMessageCc
from .types.send_message_bcc import SendMessageBcc
from .types.message_subject import MessageSubject
from .types.message_text import MessageText
from .types.message_html import MessageHtml
from .types.send_message_response import SendMessageResponse
from ..core.serialization import convert_and_respect_annotation_metadata
from ..errors.validation_error import ValidationError
from ..types.validation_error_response import ValidationErrorResponse
from ..core.client_wrapper import AsyncClientWrapper

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class MessagesClient:
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
    ) -> ListMessagesResponse:
        """
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
        ListMessagesResponse

        Examples
        --------
        from agentmail import AgentMail

        client = AgentMail(
            api_key="YOUR_API_KEY",
        )
        client.messages.list(
            inbox_id="yourinbox@agentmail.to",
            limit=10,
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v0/inboxes/{jsonable_encoder(inbox_id)}/messages",
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
                    ListMessagesResponse,
                    parse_obj_as(
                        type_=ListMessagesResponse,  # type: ignore
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
        self, inbox_id: InboxId, message_id: MessageId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Message:
        """
        Parameters
        ----------
        inbox_id : InboxId

        message_id : MessageId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Message

        Examples
        --------
        from agentmail import AgentMail

        client = AgentMail(
            api_key="YOUR_API_KEY",
        )
        client.messages.get(
            inbox_id="yourinbox@agentmail.to",
            message_id="msg_123",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v0/inboxes/{jsonable_encoder(inbox_id)}/messages/{jsonable_encoder(message_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    Message,
                    parse_obj_as(
                        type_=Message,  # type: ignore
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

    def get_attachment(
        self,
        inbox_id: InboxId,
        message_id: MessageId,
        attachment_id: AttachmentId,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Iterator[bytes]:
        """
        Parameters
        ----------
        inbox_id : InboxId

        message_id : MessageId

        attachment_id : AttachmentId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Yields
        ------
        typing.Iterator[bytes]
        """
        with self._client_wrapper.httpx_client.stream(
            f"v0/inboxes/{jsonable_encoder(inbox_id)}/messages/{jsonable_encoder(message_id)}/attachments/{jsonable_encoder(attachment_id)}",
            method="GET",
            request_options=request_options,
        ) as _response:
            try:
                if 200 <= _response.status_code < 300:
                    _chunk_size = request_options.get("chunk_size", None) if request_options is not None else None
                    for _chunk in _response.iter_bytes(chunk_size=_chunk_size):
                        yield _chunk
                    return
                _response.read()
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

    def send(
        self,
        inbox_id: InboxId,
        *,
        to: SendMessageTo,
        cc: SendMessageCc,
        bcc: SendMessageBcc,
        subject: typing.Optional[MessageSubject] = OMIT,
        text: typing.Optional[MessageText] = OMIT,
        html: typing.Optional[MessageHtml] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SendMessageResponse:
        """
        Parameters
        ----------
        inbox_id : InboxId

        to : SendMessageTo

        cc : SendMessageCc

        bcc : SendMessageBcc

        subject : typing.Optional[MessageSubject]

        text : typing.Optional[MessageText]

        html : typing.Optional[MessageHtml]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SendMessageResponse

        Examples
        --------
        from agentmail import AgentMail

        client = AgentMail(
            api_key="YOUR_API_KEY",
        )
        client.messages.send(
            inbox_id="yourinbox@agentmail.to",
            to=["bob@example.com"],
            cc=["charlie@example.com"],
            bcc=["david@example.com"],
            subject="Project Discussion",
            text="Let's review the timeline for the project.",
            html="<p>Let's review the timeline for the project.</p>",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v0/inboxes/{jsonable_encoder(inbox_id)}/messages/send",
            method="POST",
            json={
                "to": convert_and_respect_annotation_metadata(object_=to, annotation=SendMessageTo, direction="write"),
                "cc": convert_and_respect_annotation_metadata(object_=cc, annotation=SendMessageCc, direction="write"),
                "bcc": convert_and_respect_annotation_metadata(
                    object_=bcc, annotation=SendMessageBcc, direction="write"
                ),
                "subject": subject,
                "text": text,
                "html": html,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    SendMessageResponse,
                    parse_obj_as(
                        type_=SendMessageResponse,  # type: ignore
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

    def reply(
        self,
        inbox_id: InboxId,
        message_id: MessageId,
        *,
        cc: SendMessageCc,
        bcc: SendMessageBcc,
        to: typing.Optional[SendMessageTo] = OMIT,
        text: typing.Optional[MessageText] = OMIT,
        html: typing.Optional[MessageHtml] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SendMessageResponse:
        """
        Parameters
        ----------
        inbox_id : InboxId

        message_id : MessageId

        cc : SendMessageCc

        bcc : SendMessageBcc

        to : typing.Optional[SendMessageTo]

        text : typing.Optional[MessageText]

        html : typing.Optional[MessageHtml]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SendMessageResponse

        Examples
        --------
        from agentmail import AgentMail

        client = AgentMail(
            api_key="YOUR_API_KEY",
        )
        client.messages.reply(
            inbox_id="yourinbox@agentmail.to",
            message_id="msg_123",
            text="Thanks for the update. Let's meet tomorrow at 2 PM.",
            html="<p>Thanks for the update. Let's meet tomorrow at 2 PM.</p>",
            cc=["charlie@example.com"],
            bcc=["david@example.com"],
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v0/inboxes/{jsonable_encoder(inbox_id)}/messages/{jsonable_encoder(message_id)}/reply",
            method="POST",
            json={
                "to": convert_and_respect_annotation_metadata(object_=to, annotation=SendMessageTo, direction="write"),
                "cc": convert_and_respect_annotation_metadata(object_=cc, annotation=SendMessageCc, direction="write"),
                "bcc": convert_and_respect_annotation_metadata(
                    object_=bcc, annotation=SendMessageBcc, direction="write"
                ),
                "text": text,
                "html": html,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    SendMessageResponse,
                    parse_obj_as(
                        type_=SendMessageResponse,  # type: ignore
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


class AsyncMessagesClient:
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
    ) -> ListMessagesResponse:
        """
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
        ListMessagesResponse

        Examples
        --------
        import asyncio

        from agentmail import AsyncAgentMail

        client = AsyncAgentMail(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.messages.list(
                inbox_id="yourinbox@agentmail.to",
                limit=10,
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v0/inboxes/{jsonable_encoder(inbox_id)}/messages",
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
                    ListMessagesResponse,
                    parse_obj_as(
                        type_=ListMessagesResponse,  # type: ignore
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
        self, inbox_id: InboxId, message_id: MessageId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Message:
        """
        Parameters
        ----------
        inbox_id : InboxId

        message_id : MessageId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Message

        Examples
        --------
        import asyncio

        from agentmail import AsyncAgentMail

        client = AsyncAgentMail(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.messages.get(
                inbox_id="yourinbox@agentmail.to",
                message_id="msg_123",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v0/inboxes/{jsonable_encoder(inbox_id)}/messages/{jsonable_encoder(message_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    Message,
                    parse_obj_as(
                        type_=Message,  # type: ignore
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

    async def get_attachment(
        self,
        inbox_id: InboxId,
        message_id: MessageId,
        attachment_id: AttachmentId,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.AsyncIterator[bytes]:
        """
        Parameters
        ----------
        inbox_id : InboxId

        message_id : MessageId

        attachment_id : AttachmentId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Yields
        ------
        typing.AsyncIterator[bytes]
        """
        async with self._client_wrapper.httpx_client.stream(
            f"v0/inboxes/{jsonable_encoder(inbox_id)}/messages/{jsonable_encoder(message_id)}/attachments/{jsonable_encoder(attachment_id)}",
            method="GET",
            request_options=request_options,
        ) as _response:
            try:
                if 200 <= _response.status_code < 300:
                    _chunk_size = request_options.get("chunk_size", None) if request_options is not None else None
                    async for _chunk in _response.aiter_bytes(chunk_size=_chunk_size):
                        yield _chunk
                    return
                await _response.aread()
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

    async def send(
        self,
        inbox_id: InboxId,
        *,
        to: SendMessageTo,
        cc: SendMessageCc,
        bcc: SendMessageBcc,
        subject: typing.Optional[MessageSubject] = OMIT,
        text: typing.Optional[MessageText] = OMIT,
        html: typing.Optional[MessageHtml] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SendMessageResponse:
        """
        Parameters
        ----------
        inbox_id : InboxId

        to : SendMessageTo

        cc : SendMessageCc

        bcc : SendMessageBcc

        subject : typing.Optional[MessageSubject]

        text : typing.Optional[MessageText]

        html : typing.Optional[MessageHtml]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SendMessageResponse

        Examples
        --------
        import asyncio

        from agentmail import AsyncAgentMail

        client = AsyncAgentMail(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.messages.send(
                inbox_id="yourinbox@agentmail.to",
                to=["bob@example.com"],
                cc=["charlie@example.com"],
                bcc=["david@example.com"],
                subject="Project Discussion",
                text="Let's review the timeline for the project.",
                html="<p>Let's review the timeline for the project.</p>",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v0/inboxes/{jsonable_encoder(inbox_id)}/messages/send",
            method="POST",
            json={
                "to": convert_and_respect_annotation_metadata(object_=to, annotation=SendMessageTo, direction="write"),
                "cc": convert_and_respect_annotation_metadata(object_=cc, annotation=SendMessageCc, direction="write"),
                "bcc": convert_and_respect_annotation_metadata(
                    object_=bcc, annotation=SendMessageBcc, direction="write"
                ),
                "subject": subject,
                "text": text,
                "html": html,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    SendMessageResponse,
                    parse_obj_as(
                        type_=SendMessageResponse,  # type: ignore
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

    async def reply(
        self,
        inbox_id: InboxId,
        message_id: MessageId,
        *,
        cc: SendMessageCc,
        bcc: SendMessageBcc,
        to: typing.Optional[SendMessageTo] = OMIT,
        text: typing.Optional[MessageText] = OMIT,
        html: typing.Optional[MessageHtml] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SendMessageResponse:
        """
        Parameters
        ----------
        inbox_id : InboxId

        message_id : MessageId

        cc : SendMessageCc

        bcc : SendMessageBcc

        to : typing.Optional[SendMessageTo]

        text : typing.Optional[MessageText]

        html : typing.Optional[MessageHtml]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SendMessageResponse

        Examples
        --------
        import asyncio

        from agentmail import AsyncAgentMail

        client = AsyncAgentMail(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.messages.reply(
                inbox_id="yourinbox@agentmail.to",
                message_id="msg_123",
                text="Thanks for the update. Let's meet tomorrow at 2 PM.",
                html="<p>Thanks for the update. Let's meet tomorrow at 2 PM.</p>",
                cc=["charlie@example.com"],
                bcc=["david@example.com"],
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v0/inboxes/{jsonable_encoder(inbox_id)}/messages/{jsonable_encoder(message_id)}/reply",
            method="POST",
            json={
                "to": convert_and_respect_annotation_metadata(object_=to, annotation=SendMessageTo, direction="write"),
                "cc": convert_and_respect_annotation_metadata(object_=cc, annotation=SendMessageCc, direction="write"),
                "bcc": convert_and_respect_annotation_metadata(
                    object_=bcc, annotation=SendMessageBcc, direction="write"
                ),
                "text": text,
                "html": html,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    SendMessageResponse,
                    parse_obj_as(
                        type_=SendMessageResponse,  # type: ignore
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
