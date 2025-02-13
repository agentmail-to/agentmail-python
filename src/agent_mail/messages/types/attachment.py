# This file was auto-generated by Fern from our API Definition.

from ...core.pydantic_utilities import UniversalBaseModel
from .attachment_id import AttachmentId
import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2
import typing


class Attachment(UniversalBaseModel):
    attachment_id: AttachmentId
    filename: str = pydantic.Field()
    """
    Filename of attachment.
    """

    mime_type: str = pydantic.Field()
    """
    MIME type of attachment.
    """

    size: int = pydantic.Field()
    """
    Size of attachment in bytes.
    """

    inline: bool = pydantic.Field()
    """
    Whether attachment is part of message body.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
