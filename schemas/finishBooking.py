from pydantic import BaseModel


class FinishedBooking(BaseModel):
    isFinished: bool


class BookingToFinish(BaseModel):
    mail_hairdresser: str
    idBooking: str
