from .IDataBase import IDataBase
from schemas.client import Client, SavedClient
from schemas.hairdresser import Hairdresser, SavedHairdresser
from schemas.booking import BookingToSave, SavedBooking
from datetime import datetime
from typing import List

from bson.objectid import ObjectId


class DBError(Exception):
    pass


class AppDataBase(IDataBase):
    def __init__(self, client, db_name) -> None:
        self.__client = client
        self.__db = self.__client[db_name]
        self.__category_client = "Client"
        self.__category_hairdresser = "Hairdresser"

    def __row_get_str_id(self, dict_data, key_final=None):
        if key_final is not None:
            dict_data[key_final] = str(dict_data["_id"])
            dict_data.pop('_id')
        else:
            dict_data['_id'] = str(dict_data["_id"])
        return dict_data
    
    def __get_str_id(self, records, key_final=None) -> list:
        id_str_records = list(map(lambda x: self.__row_get_str_id(x, key_final=key_final), records))
        return id_str_records

    def __get_user(self, category: str, email: str):
        user_collection = self.__db['user']
        conditions = [
            { "type":{"$exists": True} },
            { "type":{"$eq": category} },
            { "email":{"$exists": True} },
            { "email": {"$eq": email} },
        ]
        proposition = {
            "$and": conditions
        }
        found_user_obj = user_collection.find(proposition)
        found_user = self.__get_str_id(found_user_obj, key_final="id")  # return list
        return found_user

    def get_client(self, email: str) -> List[SavedClient]:
        found_user = self.__get_user(self.__category_client, email)
        return found_user

    def get_hairdresser(self, email: str) -> List[SavedHairdresser]:
        found_user = self.__get_user(self.__category_hairdresser, email)
        return found_user

    def create_client(self, client: Client) -> str:
        user_collection = self.__db["user"]
        searched_user = self.get_client(client.email)
        if len(searched_user) == 0:
            document_client = client.model_dump()
            document_client['type'] = self.__category_client
            result_insert = user_collection.insert_one(document_client)
            return str(result_insert.inserted_id)
        else:
            raise DBError("There is exist user - client")

    def create_hairdresser(self, hairdresser: Hairdresser) -> str:
        user_collection = self.__db["user"]
        searched_user = self.get_hairdresser(hairdresser.email)
        if len(searched_user) == 0:
            document_hairdresser = hairdresser.model_dump()
            document_hairdresser['type'] = self.__category_hairdresser
            result_insert = user_collection.insert_one(document_hairdresser)
            return str(result_insert.inserted_id)
        else:
            raise DBError("There is exist user - hairdresser")
        
    def get_booking(self, email_hairdresser: str, datetime_start: datetime, datetime_end: datetime) -> List[SavedBooking]:
        booking_collection = self.__db['booking']
        conditions = [
            { "email_hairdresser": {"$exists": True} },
            { "email_hairdresser": {"$eq": email_hairdresser} },
            { "datetime_start": {"$exists": True} },
            { "datetime_start": {"$gte": datetime_start, "$lt": datetime_end}}   
        ]
        proposition = {
            "$and": conditions
        }
        found_booking_obj = booking_collection.find(proposition)
        found_booking = self.__get_str_id(found_booking_obj, key_final="id")  # return list
        return found_booking

    def create_booking(self, booking_to_save: BookingToSave) -> str:
        booking_collection = self.__db["booking"]
        document_booking = booking_to_save.dict()
        result_insert = booking_collection.insert_one(document_booking)
        return str(result_insert.inserted_id)

    def is_assigned_hairdresser(self, id_booking: str, email_hairdresser: str):
        booking_collection = self.__db['booking']
        conditions = [
            { "email_hairdresser": {"$exists": True} },
            { "email_hairdresser": {"$eq": email_hairdresser} },
            {'_id': ObjectId(id_booking)},  
        ]
        proposition = {
            "$and": conditions
        }
        found_booking = list(booking_collection.find(proposition))
        is_assigned = True if len(found_booking) > 0 else False
        return is_assigned
    
    def update_status_booking(self, id_booking: str, status: str) -> bool:  # return ID
        booking_collection = self.__db['booking']
        result = booking_collection.update_one(
            {'_id': ObjectId(id_booking)}, 
            {'$set': {"status": status}}
        )
        return result.acknowledged