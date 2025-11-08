# FastAPI Neon Jobs

This project is a FastAPI application that provides APIs for displaying job listings based on user niches and for posting user-selected jobs to an agency's dashboard. It uses a Neon PostgreSQL database for data storage.

## Features

- **Job Listings API**: Retrieve job listings filtered by user niche.
- **Post Jobs API**: Submit user-selected jobs to the agency's dashboard.
- **Database Integration**: Utilizes Neon PostgreSQL for persistent data storage.

## Project Structure

```
fastapi-neon-jobs
├── app
│   ├── main.py                # Entry point of the FastAPI application
│   ├── api
│   │   └── v1
│   │       ├── __init__.py    # Initializes the API versioning module
│   │       └── routers
│   │           ├── listings.py # API endpoint for job listings
│   │           └── post_jobs.py# API endpoint for posting jobs
│   ├── core
│   │   └── config.py          # Configuration settings
│   ├── db
│   │   ├── base.py            # Base class for SQLAlchemy models
│   │   ├── session.py         # Database session management
│   │   └── models
│   │       ├── job.py         # Job model definition
│   │       └── agency.py      # Agency model definition
│   ├── schemas
│   │   └── job.py             # Pydantic schemas for job data
│   ├── services
│   │   └── agency_client.py    # Service functions for agency interactions
│   └── utils
│       └── neon.py            # Utility functions for database operations
├── alembic
│   ├── env.py                 # Alembic environment configuration
│   └── versions               # Migration scripts
├── tests
│   ├── test_listings.py       # Unit tests for job listings API
│   └── test_post_jobs.py      # Unit tests for post jobs API
├── .env.example               # Example environment variables
├── requirements.txt           # Project dependencies
├── alembic.ini                # Alembic configuration file
├── Dockerfile                 # Docker image instructions
├── docker-compose.yml         # Docker services configuration
├── pyproject.toml             # Project dependencies and settings
└── README.md                  # Project documentation
```

## Setup Instructions

1. **Clone the repository**:
   ```
   git clone <repository-url>
   cd fastapi-neon-jobs
   ```

2. **Create a virtual environment**:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies**:
   ```
   pip install -r requirements.txt
   ```

4. **Set up the database**:
   - Create a `.env` file based on `.env.example` and configure your database connection.

5. **Run the application**:
   ```
   uvicorn app.main:app --reload
   ```

## Usage

- **Get Job Listings**: Send a GET request to `/api/v1/listings?Niche=<niche>`.
- **Post a Job**: Send a POST request to `/api/v1/post_jobs` with job details in the request body.

## License

This project is licensed under the MIT License.