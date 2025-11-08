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

def test_post_job():
    response = client.post(
        "/api/v1/jobs/",
        json={
            "title": "Software Engineer",
            "description": "Develop and maintain software applications.",
            "niche": "IT"
        }
    )
    assert response.status_code == 201
    assert response.json()["title"] == "Software Engineer"

def test_post_job_invalid_data():
    response = client.post(
        "/api/v1/jobs/",
        json={
            "title": "",
            "description": "No title provided.",
            "niche": "IT"
        }
    )
    assert response.status_code == 422

def test_post_job_duplicate():
    client.post(
        "/api/v1/jobs/",
        json={
            "title": "Software Engineer",
            "description": "Develop and maintain software applications.",
            "niche": "IT"
        }
    )
    response = client.post(
        "/api/v1/jobs/",
        json={
            "title": "Software Engineer",
            "description": "Duplicate job posting.",
            "niche": "IT"
        }
    )
    assert response.status_code == 400
    assert "already exists" in response.json()["detail"]