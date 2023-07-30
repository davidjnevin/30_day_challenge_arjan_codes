from fastapi.testclient import TestClient
from sqlalchemy import StaticPool, create_engine
from sqlalchemy.orm import sessionmaker

from models import Base
from main import app, get_db

SQLALCHEMY_DATABASE_URL = "sqlite:///:memory:"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={
        "check_same_thread": False,
    },
    poolclass=StaticPool,
)
Base.metadata.create_all(bind=engine)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def override_get_db():
    database = TestingSessionLocal()
    yield database
    database.close()


app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)


def test_event_not_exists():
    response = client.get(f"/events/{0}")
    assert response.status_code == 404, response.text


def test_delete_event_not_exists():
    response = client.delete(f"/events/{0}")
    assert response.status_code == 404, response.text


def test_no_available_tickets():
    event_data = {
        "title": "Test event",
        "location": "Test location",
        "start_date": "2023-09-22 12:00:00",
        "end_date": "2023-09-22 14:00:00",
        "available_tickets": 0,
    }

    response = client.post("/events", json=event_data)
    assert response.status_code == 200

    ticket_data = {
        "event_id": 1,
        "customer_name": "Jon Doe",
        "customer_email": "test@example.com",
    }

    response = client.post("/tickets", json=ticket_data)

    assert response.status_code == 400, response.text
    data = response.json()
    assert data["detail"] == "No available tickets"
