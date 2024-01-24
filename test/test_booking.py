from fastapi.testclient import TestClient
from datetime import datetime, timedelta

from main import app
import random


client = TestClient(app)


def test_new_booking():
    # Create client
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
    services = ["Service 1"]
    num_hairdresser = random.randint(1, 10000)
    email_hairdresser =  f"user{num_hairdresser}@example.com"
    # Create hairdresser
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
    # Create Booking
    now = datetime.now()
    start_booking = (now + timedelta(days=1))
    start_booking = start_booking.replace(minute=30)
    end_booking = start_booking + timedelta(minutes=30)
    datetime_start = datetime.strftime(start_booking, "%Y-%m-%d %H:%M:%S")
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
    res = response.json()
    id_booking = res['idBooking']
    assert response.status_code == 200  
    assert res['isCreated']
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
