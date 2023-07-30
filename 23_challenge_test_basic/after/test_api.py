from fastapi.testclient import TestClient
from sqlalchemy import StaticPool, create_engine
from sqlalchemy.orm import sessionmaker

from main import app, get_db
from models import Base

# Create a test database
SQLALCHEMY_DATABASE_URL = "sqlite:///memory"
engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
)

Base.metadata.create_all(bind=engine)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()


# Override the get_db function to use the test database
app.dependency_overrides[get_db] = override_get_db

# Create a test client
test_client = TestClient(app)


def test_create_event() -> None:
    event_data = {
        "title": "Test Event",
        "location": "Test location",
        "start_date": "2023-09-22 12:00:00",
        "end_date": "2023-09-22 14:00:00",
        "available_tickets": 100,
    }
    response = test_client.post("/events", json=event_data)
    event = response.json()
    assert (
        "id" in event
        and event["title"] == event_data["title"]
        and event["available_tickets"] == event_data["available_tickets"]
    )
