from pydantic import BaseModel, constr, EmailStr


SERVICES_HAIRDRESSER = ("Service 1", "Service 2", "Service 3")
SERVICES_PATTERN = "|".join(SERVICES_HAIRDRESSER)

services_pattern = constr(pattern=f'^({SERVICES_PATTERN})$')

class CreatedHairdresser(BaseModel):
    isCreated: bool


class Hairdresser(BaseModel):
    name: str
    email: EmailStr
    phone: str
    services: list[services_pattern]


class ServiceHairdresser(BaseModel):
    service: services_pattern


class SavedHairdresser(Hairdresser):
    id: str

