from typing import Optional
from pydantic import BaseModel


class CreateInboxRequest(BaseModel):
    username: Optional[str] = None
    domain: Optional[str] = None


class CreateInboxResponse(BaseModel):
    address: str
