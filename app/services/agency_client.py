from sqlalchemy.orm import Session
from app.db.models.job import Job
from app.schemas.job import JobCreate

def get_job_listings(db: Session, niche: str):
    return db.query(Job).filter(Job.niche == niche).all()

def post_job(db: Session, job: JobCreate):
    db_job = Job(**job.dict())
    db.add(db_job)
    db.commit()
    db.refresh(db_job)
    return db_job