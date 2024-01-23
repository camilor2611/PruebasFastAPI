from abc import ABC, abstractmethod
from schemas.client import Client, SavedClient
from schemas.hairdresser import Hairdresser, SavedHairdresser
from schemas.booking import BookingToSave, SavedBooking
from datetime import datetime
from typing import List


class IDataBase(ABC):
    @abstractmethod
    def get_client(self, email: str) -> List[SavedClient]:
        pass

    @abstractmethod
    def get_hairdresser(self, email: str) -> List[SavedHairdresser]:
        pass

    @abstractmethod
    def create_client(self, client: Client) -> str:  # return ID
        pass

    @abstractmethod
    def create_hairdresser(self, hairdresser: Hairdresser) -> str:  # return ID
        pass

    @abstractmethod
    def get_booking(self, email_hairdresser: str, datetime_start: datetime, datetime_end: datetime) -> List[SavedBooking]:
        pass

    @abstractmethod
    def create_booking(self, booking: BookingToSave) -> str:  # return ID
        pass

    @abstractmethod
    def is_assigned_hairdresser(self, id_booking: str, email_hairdresser: str) -> bool:  # return ID
        pass
    
    @abstractmethod
    def update_status_booking(self, id_booking: str, status: str) -> bool:
        pass