from fastapi.testclient import TestClient
from datetime import datetime, timedelta

from main import app
import random


client = TestClient(app)


def new_client():
    num_client = random.randint(1, 10000)
    email_client = f"user{num_client}@example.com"
    response = client.post(
        "/client/new-client",
        json = {
            "name": f"User {num_client}",
            "phone": 3001234567,
            "email": email_client
        },
    )
    assert response.status_code == 200
    assert response.json() == {"isCreated": True}
    return email_client


def new_hairdresser(services: list):
    num_hairdresser = random.randint(1, 10000)
    email_hairdresser =  f"user{num_hairdresser}@example.com"
    response = client.post(
        "/hairdresser/new-hairdresser",
        json = {
            "name": f"User {num_hairdresser}",
            "phone": 3001234567,
            "email": email_hairdresser,
            "services": services
        },
    )
    assert response.status_code == 200
    assert response.json() == {"isCreated": True}
    return email_hairdresser


def create_booking(email_client: str, email_hairdresser: str, services: list, datetime_start=None, datetime_end=None):
    now = datetime.now()
    start_booking = (now + timedelta(days=1))
    start_booking = start_booking.replace(minute=30)
    end_booking = start_booking + timedelta(minutes=30)
    if datetime_start is None:
        datetime_start = datetime.strftime(start_booking, "%Y-%m-%d %H:%M:%S")
    if datetime_end is None:
        datetime_end = datetime.strftime(end_booking, "%Y-%m-%d %H:%M:%S")
    response = client.post(
        "/client/new-booking",
        json = {
            "service": services[0],
            "email_client": email_client,
            "email_hairdresser": email_hairdresser,
            "datetime_start": datetime_start,
            "datetime_end": datetime_end
        }
    )
    return response, datetime_start, datetime_end


def finish_booking(email_hairdresser: str, id_booking: str):
    response = client.post(
        "/hairdresser/finish-booking",
        json = {
            "mail_hairdresser": email_hairdresser,
            "idBooking": id_booking,
        }
    )
    res = response.json()
    assert response.status_code == 200  
    assert res['isFinished']


def test_new_booking():
    services = ["Service 1"]
    email_client = new_client()
    email_hairdresser = new_hairdresser(services)
    response, datetime_start, datetime_end = create_booking(email_client, email_hairdresser, services)
    res = response.json()
    id_booking = res['idBooking']
    assert response.status_code == 200  
    assert res['isCreated']
    # validate the creation of the same booking
    response, _, _ = create_booking(email_client, email_hairdresser, services, datetime_start, datetime_end)
    assert response.status_code == 409
    assert response.json() == { "detail": "There is a booking in those dates" }
    finish_booking(email_hairdresser, id_booking)
    # the fisrt booking is finished then you can create other
    response, _, _ = create_booking(email_client, email_hairdresser, services, datetime_start, datetime_end)
    assert response.status_code == 200  
    assert res['isCreated']