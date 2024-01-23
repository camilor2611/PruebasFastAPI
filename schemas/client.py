from pydantic import BaseModel


class CreatedClient(BaseModel):
    isCreated: bool


class Client(BaseModel):
    name: str
    phone: str
    email: str
