from fastapi.testclient import TestClient

from main import app


def test_create_application_returns_saved_application():
    client = TestClient(app)

    response = client.post(
        "/application",
        json={
            "id": 1,
            "name": "John Doe",
            "credit_rating": 50,
            "homeowner": True,
        },
    )

    assert response.status_code == 200
    assert response.json() == {
        "id": 1,
        "name": "John Doe",
        "credit_rating": 50,
        "homeowner": True,
    }
