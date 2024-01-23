from pydantic import BaseModel


class FinishedBooking(BaseModel):
    isCreated: bool


class BookingToFinish(BaseModel):
    mail_hairdresser: str
    idBooking: str
