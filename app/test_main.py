from fastapi.testclient import TestClient

from main import app


def test_create_application_returns_approval_decision():
    client = TestClient(app)

    response = client.post(
        "/application",
        json={
            "id": 1,
            "name": "John Doe",
            "credit_rating": 800,
            "homeowner": True,
        },
    )

    assert response.status_code == 200
    assert response.json() == {
        "application_id": 1,
        "decision": "approved",
    }


def test_create_application_returns_decline_decision_for_high_risk_application():
    client = TestClient(app)

    response = client.post(
        "/application",
        json={
            "id": 2,
            "name": "Jane Doe",
            "credit_rating": 650,
            "homeowner": True,
        },
    )

    assert response.status_code == 200
    assert response.json() == {
        "application_id": 2,
        "decision": "declined",
    }
