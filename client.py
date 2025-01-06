import httpx
from typing import Optional, List, Union
from pydantic import BaseModel, EmailStr

from models import ClientError, ServerError, Inbox, CreateInbox, Emails, Email, SendEmail


class AgentMail:
    def __init__(self, base_url: str):
        self.base_url = base_url

    def _request(self, method: str, path: str, body: Optional[BaseModel] = None):
        json = body.model_dump(exclude_none=True) if body else None
        response = httpx.request(method, f"{self.base_url}{path}", json=json)

        if response.is_client_error:
            raise Exception(ClientError(**response.json()))
        if response.is_server_error:
            raise Exception(ServerError(**response.json()))

        if response.status_code == 204:
            return None
        return response.json()

    def create_inbox(self, username: Optional[str] = None, domain: Optional[str] = None):
        body = CreateInbox(username=username, domain=domain)
        response = self._request("POST", "/inboxes", body)
        return Inbox(**response)

    def delete_inbox(self, address: str):
        self._request("DELETE", f"/inboxes/{address}")
        return "Success"

    def get_emails(self, address: str):
        response = self._request("GET", f"/inboxes/{address}/emails")
        return Emails(**response)

    def get_email(self, address: str, id: str):
        response = self._request("GET", f"/inboxes/{address}/emails/{id}")
        return Email(**response)

    def get_sent_emails(self, address: str):
        response = self._request("GET", f"/inboxes/{address}/sent")
        return Emails(**response)

    def get_sent_email(self, address: str, id: str):
        response = self._request("GET", f"/inboxes/{address}/sent/{id}")
        return Email(**response)

    def send_email(
        self,
        address: str,
        to: Optional[Union[EmailStr, List[EmailStr]]] = None,
        cc: Optional[Union[EmailStr, List[EmailStr]]] = None,
        bcc: Optional[Union[EmailStr, List[EmailStr]]] = None,
        subject: Optional[str] = None,
        text: Optional[str] = None,
    ):
        body = SendEmail(to=to, cc=cc, bcc=bcc, subject=subject, text=text)
        self._request("POST", f"/inboxes/{address}/sent", body)
        return "Success"

    def reply_to_email(
        self,
        address: str,
        id: str,
        to: Optional[Union[EmailStr, List[EmailStr]]] = None,
        cc: Optional[Union[EmailStr, List[EmailStr]]] = None,
        bcc: Optional[Union[EmailStr, List[EmailStr]]] = None,
        subject: Optional[str] = None,
        text: Optional[str] = None,
    ):
        body = SendEmail(to=to, cc=cc, bcc=bcc, subject=subject, text=text)
        self._request("POST", f"/inboxes/{address}/emails/{id}/reply", body)
        return "Success"
