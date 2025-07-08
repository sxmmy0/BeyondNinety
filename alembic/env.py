import asyncio
import os
import sys
from logging.config import fileConfig

from alembic import context
from sqlalchemy.ext.asyncio import async_engine_from_config
from sqlalchemy.ext.asyncio import AsyncEngine
from sqlalchemy import pool
from dotenv import load_dotenv

# Load .env for DB credentials
load_dotenv(os.path.join(os.path.dirname(__file__), '..', '.env'))

# Add app directory to sys.path
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'byd90'))

from app.core.database import Base
from app.models import user, coach, avatar  # ensure all models are imported

# Alembic Config object
config = context.config
fileConfig(config.config_file_name)

# Inject URL from env
db_url = os.environ.get("DATABASE_URL")

# Swap out 'db' with 'localhost' if not running in Docker
if db_url and "db" in db_url and os.environ.get("RUNNING_IN_DOCKER") != "1":
    db_url = db_url.replace("@db", "@localhost")

config.set_main_option("sqlalchemy.url", db_url)
target_metadata = Base.metadata


def run_migrations_offline() -> None:
    """Run migrations without a DB connection."""
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


async def run_migrations_online() -> None:
    """Run migrations with a live DB connection."""
    connectable: AsyncEngine = async_engine_from_config(
        config.get_section(config.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    async with connectable.begin() as connection:
        def do_run_migrations(connection):
            context.configure(
                connection=connection,
                target_metadata=target_metadata,
            )
            with context.begin_transaction():
                context.run_migrations()

        await connection.run_sync(do_run_migrations)

    await connectable.dispose()

