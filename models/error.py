from pydantic import BaseModel


class ClientError(BaseModel):
    message: str


class ServerError(BaseModel):
    message: str
