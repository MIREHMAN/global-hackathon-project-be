from fastapi.testclient import TestClient
from app.main import app
from app.db.session import get_db
from app.db.models.job import Job
from sqlalchemy.orm import Session

client = TestClient(app)

def override_get_db():
    db = next(get_db())
    try:
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

def test_get_job_listings():
    response = client.get("/api/v1/listings?Niche=IT")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_post_job_listing():
    job_data = {
        "title": "Software Engineer",
        "description": "Develop and maintain software applications.",
        "niche": "IT"
    }
    response = client.post("/api/v1/post_jobs", json=job_data)
    assert response.status_code == 201
    assert response.json()["title"] == job_data["title"]

def test_get_job_listings_empty_niche():
    response = client.get("/api/v1/listings?Niche=NonExistentNiche")
    assert response.status_code == 200
    assert response.json() == []