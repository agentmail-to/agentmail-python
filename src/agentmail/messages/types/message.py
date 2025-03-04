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
from .message_reply_to import MessageReplyTo
import typing
from .message_subject import MessageSubject
from .message_preview import MessagePreview
from .message_to import MessageTo
from .message_cc import MessageCc
from .message_bcc import MessageBcc
from .message_text import MessageText
from .message_html import MessageHtml
from .message_attachments import MessageAttachments
from .message_in_reply_to import MessageInReplyTo
from .message_references import MessageReferences
from ...inboxes.types.inbox_id import InboxId
from ...types.organization_id import OrganizationId
from ...core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic


class Message(UniversalBaseModel):
    """
    Examples
    --------
    import datetime

    from agentmail.messages import Attachment, Message

    Message(
        message_id="msg_123",
        thread_id="thread_123",
        event_id="event_123",
        labels=["RECEIVED", "UNREAD"],
        timestamp=datetime.datetime.fromisoformat(
            "2024-01-15 09:30:00+00:00",
        ),
        from_="alice@example.com",
        reply_to="alice.work@example.com",
        to=["bob@example.com"],
        cc=["charlie@example.com"],
        bcc=["david@example.com"],
        subject="Project Discussion",
        preview="Let's review the timeline for the project.",
        text="Let's review the timeline for the project. How does tomorrow look?",
        html="<p>Let's review the timeline for the project. How does tomorrow look?</p>",
        attachments=[
            Attachment(
                attachment_id="att_123",
                filename="proposal.pdf",
                content_type="application/pdf",
                size=1024,
                inline=False,
            )
        ],
        in_reply_to="msg_122",
        references=["msg_121", "msg_122"],
        inbox_id="yourinbox@agentmail.to",
        organization_id="org_123",
    )
    """

    thread_id: ThreadId
    message_id: MessageId
    event_id: MessageEventId
    labels: MessageLabels
    timestamp: MessageTimestamp
    from_: typing_extensions.Annotated[MessageFrom, FieldMetadata(alias="from")]
    reply_to: MessageReplyTo
    subject: typing.Optional[MessageSubject] = None
    preview: typing.Optional[MessagePreview] = None
    to: MessageTo
    cc: typing.Optional[MessageCc] = None
    bcc: typing.Optional[MessageBcc] = None
    text: typing.Optional[MessageText] = None
    html: typing.Optional[MessageHtml] = None
    attachments: typing.Optional[MessageAttachments] = None
    in_reply_to: MessageInReplyTo
    references: MessageReferences
    inbox_id: InboxId
    organization_id: OrganizationId

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
