# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...types.count import Count
from ...types.last_key import LastKey
from ...types.limit import Limit
from .draft_item import DraftItem


class ListDraftsResponse(UniversalBaseModel):
    count: Count
    limit: typing.Optional[Limit] = None
    last_key: typing.Optional[LastKey] = None
    drafts: typing.List[DraftItem] = pydantic.Field()
    """
    Draft items. Ordered by `updated_at` descending.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
