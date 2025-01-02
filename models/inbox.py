from typing import Optional
from pydantic import BaseModel


class CreateInbox(BaseModel):
    username: Optional[str] = None
    domain: Optional[str] = None


class Inbox(BaseModel):
    address: str
