from pydantic import BaseModel, EmailStr, field_validator
from datetime import datetime
from .hairdresser import ServiceHairdresser


class CreatedBook(BaseModel):
    idBooking: str
    isCreated: bool


class Booking(ServiceHairdresser):
    email_client: EmailStr
    email_hairdresser: EmailStr
    datetime_start: str
    datetime_end: str    

    @field_validator("datetime_start", "datetime_end")
    def ensure_date_range(cls, val):
        datetime.strptime(val, '%Y-%m-%d %H:%M:%S')
        return val


class BookingToSave(ServiceHairdresser):
    email_client: EmailStr
    email_hairdresser: EmailStr
    datetime_start: datetime
    datetime_end: datetime
    status: str


class SavedBooking(Booking):
    status: str
    id: str
