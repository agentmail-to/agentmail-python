import httpx
from typing import Optional

from models import CreateInboxRequest, CreateInboxResponse


class AgentMail:
    def __init__(self, base_url: str):
        self.base_url = base_url

    def create_inbox(self, username: Optional[str] = None, domain: Optional[str] = None):
        body = CreateInboxRequest(username=username, domain=domain)
        response = httpx.post(f"{self.base_url}/inboxes", json=body.model_dump(exclude_none=True))
        response.raise_for_status()
        return CreateInboxResponse(**response.json())

    def delete_inbox(self, address: str):
        response = httpx.delete(f"{self.base_url}/inboxes/{address}")
        response.raise_for_status()
        return response.status_code
