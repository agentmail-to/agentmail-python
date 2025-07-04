# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2
from ...core.unchecked_base_model import UncheckedBaseModel
from .client_id import ClientId
from .event_types import EventTypes
from .inbox_ids import InboxIds
from .url import Url
from .webhook_id import WebhookId


class Webhook(UncheckedBaseModel):
    webhook_id: WebhookId
    url: Url
    event_types: typing.Optional[EventTypes] = None
    inbox_ids: typing.Optional[InboxIds] = None
    secret: str = pydantic.Field()
    """
    Secret for webhook signature verification.
    """

    enabled: bool = pydantic.Field()
    """
    Whether the webhook is enabled.
    """

    updated_at: dt.datetime = pydantic.Field()
    """
    Time at which webhook was last updated.
    """

    created_at: dt.datetime = pydantic.Field()
    """
    Time at which webhook was created.
    """

    client_id: typing.Optional[ClientId] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
