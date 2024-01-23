from pydantic import BaseModel, constr


SERVICES_HAIRDRESSER = ("Service 1", "Service 2", "Service 3")
SERVICES_PATTERN = "|".join(SERVICES_HAIRDRESSER)

ContactConstr = constr(pattern=f'^{SERVICES_PATTERN}$')

class CreatedHairdresser(BaseModel):
    isCreated: bool


class Hairdresser(BaseModel):
    name: str
    email: str
    services: ContactConstr


class ServiceHairdresser(BaseModel):
    service: ContactConstr