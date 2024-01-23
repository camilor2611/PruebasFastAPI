from pydantic import BaseModel, EmailStr


class CreatedClient(BaseModel):
    isCreated: bool


class Client(BaseModel):
    name: str
    phone: str
    email: EmailStr


class SavedClient(Client):
    id: str
