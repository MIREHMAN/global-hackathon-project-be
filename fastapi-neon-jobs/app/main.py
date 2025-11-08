from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.v1.routers import listings, post_jobs

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(listings.router, prefix="/api/v1/listings", tags=["job listings"])
app.include_router(post_jobs.router, prefix="/api/v1/jobs", tags=["post jobs"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the Job Listings API"}