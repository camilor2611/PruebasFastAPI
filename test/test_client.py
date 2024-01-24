from fastapi.testclient import TestClient

from main import app
import random


client = TestClient(app)


def test_new_client():
    num_ = random.randint(1, 10000)
    response = client.post(
        "/client/new-client",
        json = {
            "name": f"User {num_}",
            "phone": "000-0000-000",
            "email": f"user{num_}@example.com"
        },
    )
    assert response.status_code == 200
    assert response.json() == {
        "isCreated": True
    }


def test_error_mail():
    response = client.post(
        "/client/new-client",
        json={ 
            "name": "string",
            "phone": "string",
            "email": "userexample.com"
        },
    )
    assert response.status_code == 422
    assert response.json() == {
        "detail": [
            {
                "type": "value_error",
                "loc": [
                    "body",
                    "email"
                ],
                "msg": "value is not a valid email address: The email address is not valid. It must have exactly one @-sign.",
                "input": "userexample.com",
                "ctx": {
                    "reason": "The email address is not valid. It must have exactly one @-sign."
                }
            }
        ]
    }


