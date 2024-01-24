from pydantic import BaseModel, EmailStr, field_validator
from fastapi import HTTPException

class CreatedClient(BaseModel):
    isCreated: bool


class Client(BaseModel):
    name: str
    phone: int
    email: EmailStr

    @field_validator("phone")
    def validate_number(cls, val):
        str_number = str(val)
        if len(str_number) != 10 or str_number[0] != "3":
            raise HTTPException(status_code=409, detail="Incorrect phone number")
        return val

class SavedClient(Client):
    id: str
