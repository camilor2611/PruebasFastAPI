from pydantic import BaseModel, EmailStr, validator


class Address(BaseModel):
    address: EmailStr


class Recipients(BaseModel):
    to: list[Address]
