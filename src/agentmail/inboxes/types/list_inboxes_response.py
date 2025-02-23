# This file was auto-generated by Fern from our API Definition.

from ...core.pydantic_utilities import UniversalBaseModel
import typing
from .inbox import Inbox
import pydantic
from ...types.count import Count
from ...types.limit import Limit
from ...types.last_key import LastKey
from ...core.pydantic_utilities import IS_PYDANTIC_V2


class ListInboxesResponse(UniversalBaseModel):
    """
    Examples
    --------
    import datetime

    from agentmail.inboxes import Inbox, ListInboxesResponse

    ListInboxesResponse(
        inboxes=[
            Inbox(
                inbox_id="yourinbox@agentmail.to",
                organization_id="123e4567-e89b-12d3-a456-426614174000",
                display_name="Your Inbox",
                created_at=datetime.datetime.fromisoformat(
                    "2024-01-15 09:30:00+00:00",
                ),
            )
        ],
        limit=10,
        count=1,
        last_key="123e4567-e89b-12d3-a456-426614174000",
    )
    """

    inboxes: typing.List[Inbox] = pydantic.Field()
    """
    Inbox items. Ordered by `created_at` ascending.
    """

    count: Count
    limit: typing.Optional[Limit] = None
    last_key: typing.Optional[LastKey] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
