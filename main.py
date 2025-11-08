from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Use absolute imports only if running as a module: python -m app.main
try:
    from app.api.v1.routers import listings, post_jobs
except ModuleNotFoundError:
    # fallback if running directly as python app/main.py
    from app.api.v1.routers import listings, post_jobs

app = FastAPI(title="Job Listings API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(listings.router, prefix="/api/v1/listings", tags=["Job Listings"])
app.include_router(post_jobs.router, prefix="/api/v1/jobs", tags=["Post Jobs"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the Job Listings API"}
