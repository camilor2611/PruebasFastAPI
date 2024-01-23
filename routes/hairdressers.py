from fastapi import APIRouter
from fastapi import HTTPException
from pymongo import MongoClient
import os

from schemas.hairdresser import Hairdresser, CreatedHairdresser
from schemas.finishBooking import BookingToFinish, FinishedBooking
from infrastructure.DataBase import AppDataBase
from domain.hairdresser import DomainHairdresser


client = MongoClient(os.environ.get("connection_mongo_db"))
app_data_base = AppDataBase(client, os.environ.get("mongo_db_name"))
routes_hairdresser = APIRouter()


@routes_hairdresser.post("/new-hairdresser", response_model=CreatedHairdresser)
def new_hairdresser(req_hairdresser: Hairdresser):
    try:
        _domain_hairdresser = DomainHairdresser(app_data_base)
        _domain_hairdresser.create_hairdresser(req_hairdresser)
        return {"isCreated": True}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@routes_hairdresser.post("/finish-booking", response_model=FinishedBooking)
def finish_booking(req_finish_booking: BookingToFinish):
    try:
        _domain_hairdresser = DomainHairdresser(app_data_base)
        result = _domain_hairdresser.finish_booking(req_finish_booking)
        return {"isFinished": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))