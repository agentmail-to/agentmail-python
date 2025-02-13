# This file was auto-generated by Fern from our API Definition.

from ...core.pydantic_utilities import UniversalBaseModel
import typing
from .inbox import Inbox
import pydantic
from ...types.limit import Limit
from ...types.count import Count
from ...types.last_key import LastKey
from ...core.pydantic_utilities import IS_PYDANTIC_V2


class ListInboxesResponse(UniversalBaseModel):
    inboxes: typing.List[Inbox] = pydantic.Field()
    """
    Inbox items. Ordered by `created_at` ascending.
    """

    limit: Limit
    count: Count
    last_key: LastKey

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
