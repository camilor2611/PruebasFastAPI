from fastapi import APIRouter
from fastapi import HTTPException
from pymongo import MongoClient
import os

from schemas.client import Client, CreatedClient
from schemas.booking import CreatedBook, Booking
from infrastructure.DataBase import AppDataBase
from domain.client import DomainClient


client = MongoClient(os.environ.get("connection_mongo_db"))
app_data_base = AppDataBase(client, os.environ.get("mongo_db_name"))
routes_client = APIRouter()


@routes_client.post("/new-client", response_model=CreatedClient)
def new_client(req_client: Client):
    try:
        _client_domain = DomainClient(app_data_base)
        _client_domain.create_client(req_client)
        return {"isCreated": True}
    except Exception as e:
        raise HTTPException(status_code=409, detail=str(e))
    

@routes_client.post("/new-booking", response_model=CreatedBook)
def new_book(req_book: Booking):
    try:
        _client_domain = DomainClient(app_data_base)
        id_booking = _client_domain.create_booking(req_book)
        return {"isCreated": True, "idBooking": id_booking }
    except Exception as e:
        raise HTTPException(status_code=409, detail=str(e))