from typing import Optional, List, Union
from pydantic import BaseModel, Field, EmailStr


class EmailAddress(BaseModel):
    address: EmailStr
    name: Optional[str] = None


class EmailsItem(BaseModel):
    id: str
    timestamp: str
    from_: EmailAddress = Field(alias="from")
    subject: Optional[str] = None
    text: Optional[str] = None


class Emails(BaseModel):
    emails: List[EmailsItem]
    count: int
    limit: int
    last_key: Optional[str] = None


class Email(BaseModel):
    id: str
    timestamp: str
    from_: EmailAddress = Field(alias="from")
    reply_to: Optional[EmailAddress] = None
    to: List[EmailAddress]
    cc: Optional[List[EmailAddress]] = None
    bcc: Optional[List[EmailAddress]] = None
    subject: Optional[str] = None
    text: Optional[str] = None
    html: Optional[str] = None
    message_id: Optional[str] = None
    in_reply_to: Optional[str] = None
    references: Optional[List[str]] = None
    created_at: Optional[str] = None


class SendEmail(BaseModel):
    to: Optional[Union[EmailStr, List[EmailStr]]] = None
    cc: Optional[Union[EmailStr, List[EmailStr]]] = None
    bcc: Optional[Union[EmailStr, List[EmailStr]]] = None
    subject: Optional[str] = None
    text: Optional[str] = None
