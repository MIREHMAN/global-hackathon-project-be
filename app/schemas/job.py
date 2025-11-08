from pydantic import BaseModel
from typing import List, Optional

class JobBase(BaseModel):
    title: str
    description: str
    niche: str

class JobCreate(JobBase):
    pass

class Job(JobBase):
    id: int

    class Config:
        orm_mode = True

class JobListResponse(BaseModel):
    jobs: List[Job]