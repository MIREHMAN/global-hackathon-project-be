from logging.config import fileConfig
import os
from dotenv import load_dotenv
from sqlalchemy import engine_from_config
from sqlalchemy import pool
from alembic import context
from app.db.base import Base
from app.db.models import job, agency  # Import your models here

config = context.config

# Load .env from project root (fastapi-neon-jobs/.env)
base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
load_dotenv(os.path.join(base_dir, '.env'))

# Prefer common env var names used in your project
database_url = (
    os.getenv("DATABASE_URL")
    or os.getenv("POSTGRES_URL")
    or os.getenv("DATABASE_URL_UNPOOLED")
    or os.getenv("POSTGRES_URL_NON_POOLING")
)
if database_url:
    config.set_main_option("sqlalchemy.url", database_url)

fileConfig(config.config_file_name)

target_metadata = Base.metadata

def run_migrations_offline():
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online():
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix='sqlalchemy.',
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
        )

        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()