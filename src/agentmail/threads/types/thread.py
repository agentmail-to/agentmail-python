# This file was auto-generated by Fern from our API Definition.

from ...core.pydantic_utilities import UniversalBaseModel
from .thread_id import ThreadId
from ...inboxes.types.inbox_id import InboxId
import datetime as dt
import pydantic
from .thread_updated_at import ThreadUpdatedAt
import typing
from .thread_subject import ThreadSubject
from .thread_participants import ThreadParticipants
from ...messages.types.message import Message
from ...core.pydantic_utilities import IS_PYDANTIC_V2


class Thread(UniversalBaseModel):
    thread_id: ThreadId
    inbox_id: InboxId
    created_at: dt.datetime = pydantic.Field()
    """
    Time at which thread was created.
    """

    updated_at: ThreadUpdatedAt
    subject: typing.Optional[ThreadSubject] = None
    participants: ThreadParticipants
    messages: typing.List[Message] = pydantic.Field()
    """
    Messages in thread. Ordered by `sent_at` ascending.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
