# This file was auto-generated by Fern from our API Definition.

from ...core.pydantic_utilities import UniversalBaseModel
from .thread_id import ThreadId
from .thread_event_id import ThreadEventId
from .thread_labels import ThreadLabels
from .thread_timestamp import ThreadTimestamp
from .thread_senders import ThreadSenders
from .thread_recipients import ThreadRecipients
from .thread_message_count import ThreadMessageCount
import typing
from .thread_subject import ThreadSubject
from .thread_preview import ThreadPreview
from .thread_attachments import ThreadAttachments
from ...messages.types.message import Message
import pydantic
from ...inboxes.types.inbox_id import InboxId
from ...core.pydantic_utilities import IS_PYDANTIC_V2


class Thread(UniversalBaseModel):
    """
    Examples
    --------
    import datetime

    from agentmail.messages import Message
    from agentmail.threads import Thread

    Thread(
        inbox_id="yourinbox@agentmail.to",
        thread_id="thread_123",
        event_id="event_123",
        labels=["RECEIVED", "UNREAD"],
        timestamp=datetime.datetime.fromisoformat(
            "2024-01-15 09:30:00+00:00",
        ),
        senders=["alice@example.com"],
        recipients=["bob@example.com"],
        message_count=1,
        subject="Project Discussion",
        preview="Let's review the timeline for...",
        messages=[
            Message(
                message_id="msg_123",
                thread_id="thread_123",
                event_id="event_123",
                labels=["RECEIVED", "UNREAD"],
                timestamp=datetime.datetime.fromisoformat(
                    "2024-01-15 09:30:00+00:00",
                ),
                from_="alice@example.com",
                to=["bob@example.com"],
                text="Let's review the timeline for the project.",
                inbox_id="yourinbox@agentmail.to",
            )
        ],
    )
    """

    thread_id: ThreadId
    event_id: ThreadEventId
    labels: ThreadLabels
    timestamp: ThreadTimestamp
    senders: ThreadSenders
    recipients: ThreadRecipients
    message_count: ThreadMessageCount
    subject: typing.Optional[ThreadSubject] = None
    preview: typing.Optional[ThreadPreview] = None
    attachments: typing.Optional[ThreadAttachments] = None
    messages: typing.List[Message] = pydantic.Field()
    """
    Messages in thread. Ordered by `sent_at` ascending.
    """

    inbox_id: InboxId

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
