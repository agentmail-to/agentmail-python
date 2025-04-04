# This file was auto-generated by Fern from our API Definition.

from ...core.pydantic_utilities import UniversalBaseModel
from .inbox_id import InboxId
import pydantic
import typing
from .display_name import DisplayName
import datetime as dt
from ...core.pydantic_utilities import IS_PYDANTIC_V2


class Inbox(UniversalBaseModel):
    """
    Examples
    --------
    import datetime

    from agentmail.inboxes import Inbox

    Inbox(
        inbox_id="yourinbox@agentmail.to",
        organization_id="123e4567-e89b-12d3-a456-426614174000",
        display_name="Your Inbox",
        created_at=datetime.datetime.fromisoformat(
            "2024-01-15 09:30:00+00:00",
        ),
    )
    """

    inbox_id: InboxId
    organization_id: str = pydantic.Field()
    """
    ID of organization that owns inbox.
    """

    display_name: typing.Optional[DisplayName] = None
    created_at: dt.datetime = pydantic.Field()
    """
    Time at which inbox was created.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
