from fastapi.testclient import TestClient

from main import app
import random


client = TestClient(app)


def test_new_hairdresser():
    num_ = random.randint(1, 10000)
    response = client.post(
        "/hairdresser/new-hairdresser",
        json = {
            "name": f"User {num_}",
            "phone": 3001234567,
            "email": f"user{num_}@example.com",
            "services": [
                "Service 1"
            ]
        },
    )
    assert response.status_code == 200
    assert response.json() == {
        "isCreated": True
    }


def test_error_service():
    num_ = random.randint(1, 10000)
    incorrect_service = "Service 100"
    response = client.post(
        "/hairdresser/new-hairdresser",
        json = {
            "name": f"User {num_}",
            "phone": 3001234567,
            "email": f"user{num_}@example.com",
            "services": [
                incorrect_service
            ]
        },
    )
    assert response.status_code == 422
    assert response.json() == {
        "detail": [
            {
            "type": "string_pattern_mismatch",
            "loc": [
                "body",
                "services",
                0
            ],
            "msg": "String should match pattern '^(Service 1|Service 2|Service 3)$'",
            "input": incorrect_service,
            "ctx": {
                "pattern": "^(Service 1|Service 2|Service 3)$"
            },
            "url": "https://errors.pydantic.dev/2.5/v/string_pattern_mismatch"
            }
        ]
        }


