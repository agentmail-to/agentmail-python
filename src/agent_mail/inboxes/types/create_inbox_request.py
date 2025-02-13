# This file was auto-generated by Fern from our API Definition.

from ...core.pydantic_utilities import UniversalBaseModel
import typing
import pydantic
from .display_name import DisplayName
from ...core.pydantic_utilities import IS_PYDANTIC_V2


class CreateInboxRequest(UniversalBaseModel):
    """
    Examples
    --------
    from agent_mail.inboxes import CreateInboxRequest

    CreateInboxRequest(
        username="yourinbox",
        display_name="Your Inbox",
    )
    """

    username: typing.Optional[str] = pydantic.Field(default=None)
    """
    Username of address. Randomly generated if not specified.
    """

    domain: typing.Optional[str] = pydantic.Field(default=None)
    """
    Domain of address. Must be verified domain. Defaults to `agentmail.to`.
    """

    display_name: typing.Optional[DisplayName] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
