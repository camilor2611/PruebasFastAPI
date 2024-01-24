from pydantic import BaseModel, constr, EmailStr, field_validator
from fastapi import HTTPException


SERVICES_HAIRDRESSER = ("Service 1", "Service 2", "Service 3")
SERVICES_PATTERN = "|".join(SERVICES_HAIRDRESSER)

services_pattern = constr(pattern=f'^({SERVICES_PATTERN})$')

class CreatedHairdresser(BaseModel):
    isCreated: bool


class Hairdresser(BaseModel):
    name: str
    email: EmailStr
    phone: int
    services: list[services_pattern]
    
    @field_validator("phone")
    def validate_number(cls, val):
        str_number = str(val)
        if len(str_number) != 10 or str_number[0] != "3":
            raise HTTPException(status_code=409, detail="Incorrect phone number")
        return val


class ServiceHairdresser(BaseModel):
    service: services_pattern


class SavedHairdresser(Hairdresser):
    id: str

