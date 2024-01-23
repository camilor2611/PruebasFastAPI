from fastapi import APIRouter
from schemas.hairdresser import Hairdresser, CreatedHairdresser
from schemas.finishBooking import BookingToFinish, FinishedBooking

routes_hairdresser = APIRouter()


@routes_hairdresser.post("/new-hairdresser", response_model=CreatedHairdresser)
def new_hairdresser(req_hairdresser: Hairdresser):
    try:
        a = "s" + 0
        return {"isCreated": True}
    except Exception as e:
        return {"msg": str(e)}


@routes_hairdresser.post("/finish-booking", response_model=FinishedBooking)
def finish_booking(req_finish_booking: BookingToFinish):
    try:
        return {"isCreated": True}
    except Exception as e:
        return {"msg": str(e)}
