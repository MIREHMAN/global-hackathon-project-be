from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.db.models.job import Job
from app.schemas.job import JobOut
from typing import List

router = APIRouter()

@router.get("/listings/{niche}", response_model=List[JobOut])
def get_job_listings(niche: str, db: Session = next(get_db())):
    job_listings = db.query(Job).filter(Job.niche == niche).all()
    if not job_listings:
        raise HTTPException(status_code=404, detail="No job listings found for this niche")
    return job_listings