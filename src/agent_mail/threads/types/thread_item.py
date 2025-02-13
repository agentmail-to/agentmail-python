# This file was auto-generated by Fern from our API Definition.

from ...core.pydantic_utilities import UniversalBaseModel
from .thread_id import ThreadId
from .thread_updated_at import ThreadUpdatedAt
from .thread_participants import ThreadParticipants
from .thread_subject import ThreadSubject
from .thread_preview import ThreadPreview
from ...core.pydantic_utilities import IS_PYDANTIC_V2
import typing
import pydantic


class ThreadItem(UniversalBaseModel):
    thread_id: ThreadId
    updated_at: ThreadUpdatedAt
    participants: ThreadParticipants
    subject: ThreadSubject
    preview: ThreadPreview

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
