# This file was auto-generated by Fern from our API Definition.

from ...core.pydantic_utilities import UniversalBaseModel
from ...threads.types.thread_id import ThreadId
from .message_id import MessageId
from .message_event_id import MessageEventId
from .message_labels import MessageLabels
from .message_timestamp import MessageTimestamp
import typing_extensions
from .message_from import MessageFrom
from ...core.serialization import FieldMetadata
from .message_to import MessageTo
import typing
from .message_cc import MessageCc
from .message_bcc import MessageBcc
from .message_subject import MessageSubject
from .message_preview import MessagePreview
from .message_attachments import MessageAttachments
from ...core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic


class MessageItem(UniversalBaseModel):
    thread_id: ThreadId
    message_id: MessageId
    event_id: MessageEventId
    labels: MessageLabels
    timestamp: MessageTimestamp
    from_: typing_extensions.Annotated[MessageFrom, FieldMetadata(alias="from")]
    to: MessageTo
    cc: typing.Optional[MessageCc] = None
    bcc: typing.Optional[MessageBcc] = None
    subject: typing.Optional[MessageSubject] = None
    preview: typing.Optional[MessagePreview] = None
    attachments: typing.Optional[MessageAttachments] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
