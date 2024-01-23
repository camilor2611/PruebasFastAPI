from pydantic import BaseModel, validator
from datetime import datetime
from .hairdresser import ServiceHairdresser


class CreatedBook(BaseModel):
    idBooking: str
    isCreated: bool


class Book(ServiceHairdresser):
    email_client: str
    email_hairdresser: str
    datetime_start: str
    datetime_end: str


    @validator("datetime_start", "datetime_end")
    def ensure_date_range(cls, val):
        datetime.strptime(val, '%Y-%m-%d %H:%M:%S')
        return val
