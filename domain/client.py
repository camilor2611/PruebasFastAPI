from datetime import datetime

from infrastructure.DataBase import AppDataBase
from schemas.booking import Booking, BookingToSave
from schemas.client import Client
from schemas.address import Address, Recipients
from handlerError import CustomError
from domain.mailAzure import send_mail
import pytz


class DomainClient():
    def __init__(self, data_base: AppDataBase) -> None:
        self.__handler_db = data_base
        self.__format_datetime = '%Y-%m-%d %H:%M:%S'
        self.__tz = pytz.timezone('America/Bogota')

    def create_client(self, client: Client) -> str:
        self.__handler_db.create_client(client)

    def create_booking(self, booking: Booking) -> str:
        document_booking = booking.model_dump()
        result_client = self.__handler_db.get_client(booking.email_client)
        result_hairdresser = self.__handler_db.get_hairdresser(booking.email_hairdresser)

        if len(result_client) == 0 or len(result_hairdresser) == 0:
            raise CustomError("There is not exist client or hairdresser")
        
        if booking.service not in result_hairdresser[0]['services']:
            raise CustomError(f"The hairdresser do not have '{booking.service}' service")
        
        date_booked = self.__handler_db.get_booking(document_booking['email_hairdresser'], document_booking['datetime_start'], document_booking['datetime_end'])
        if len(date_booked) > 0:
            raise CustomError("There is a booking in those dates")
        
        document_booking['datetime_start'] =  self.__tz.localize(
            datetime.strptime(document_booking['datetime_start'], self.__format_datetime)
        ).replace(second=0)
        document_booking['datetime_end'] = self.__tz.localize(
            datetime.strptime(document_booking['datetime_end'], self.__format_datetime) 
        ).replace(second=0)
        current_datetime = datetime.now(self.__tz)
        document_booking['status'] = "Created"
        differents_time_start_and_now = document_booking['datetime_start'] - current_datetime
        differents_time_start_and_now_seg = differents_time_start_and_now.total_seconds()
        duration_booking = document_booking['datetime_end'] - document_booking['datetime_start']
        duration_booking_seconds = duration_booking.total_seconds()
        minute_datetime_start = document_booking['datetime_start'].minute
        if (duration_booking_seconds >= 1800 and 
                duration_booking_seconds <= 7200 and 
                minute_datetime_start % 30 == 0 and 
                differents_time_start_and_now_seg > 0):
            booking_to_save = BookingToSave(**document_booking)
            result_insert_id = self.__handler_db.create_booking(booking_to_save)
            
            mail_client = Address(address=booking.email_client)
            recipients = Recipients(to=[mail_client])
            msg = f"Your reservation is created, do not forget to attend at {booking.datetime_start} to {booking.datetime_end}"
            send_mail(recipients, "Created booking", msg)
            return result_insert_id
        else:
            raise CustomError("Time out of range or date start/end invalid")

        
