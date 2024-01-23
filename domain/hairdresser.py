from infrastructure.DataBase import AppDataBase
from schemas.hairdresser import Hairdresser
from schemas.finishBooking import BookingToFinish
from handlerError import CustomError


class DomainHairdresser():
    def __init__(self, data_base: AppDataBase) -> None:
        self.__handler_db = data_base
    
    def create_hairdresser(self, hairdresser: Hairdresser) -> str:
        return self.__handler_db.create_hairdresser(hairdresser)
    
    def finish_booking(self, booking_to_finish: BookingToFinish) -> bool:
        is_assigned = self.__handler_db.is_assigned_hairdresser(booking_to_finish.idBooking, booking_to_finish.mail_hairdresser)
        if is_assigned:
            result = self.__handler_db.update_status_booking(booking_to_finish.idBooking, "Finished")
            return result
        else: 
            raise CustomError("Denied action")
