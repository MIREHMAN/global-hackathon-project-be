from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.db.models.job import Job
from app.schemas.job import JobCreate

router = APIRouter()

class PostJobResponse(BaseModel):
    message: str
    job_id: int

@router.post("/post-job", response_model=PostJobResponse)
def post_job(job: JobCreate, db: Session = next(get_db())):
    db_job = Job(**job.dict())
    db.add(db_job)
    db.commit()
    db.refresh(db_job)
    return {"message": "Job posted successfully", "job_id": db_job.id}