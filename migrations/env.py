import os
from logging.config import fileConfig
import asyncio
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy import pool
from alembic import context
from app.db.model.index import metadata
from app.config import db_url
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Alembic Config object
config = context.config

# Interpret the config file for Python logging
fileConfig(config.config_file_name)

# Update the config with the constructed URL
config.set_main_option("sqlalchemy.url", db_url)

# SQLAlchemy metadata
target_metadata = metadata


async def run_migrations_online() -> None:
    """Run migrations in 'online' mode with async engine."""
    connectable = create_async_engine(
        db_url, echo=True, poolclass=pool.NullPool  # Disable pooling for migrations
    )

    async with connectable.connect() as connection:
        # Run migrations synchronously within the async connection
        await connection.run_sync(do_run_migrations)


def do_run_migrations(connection):
    """Configure and run migrations synchronously."""
    context.configure(connection=connection, target_metadata=target_metadata)

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode."""
    context.configure(
        url=db_url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    asyncio.run(run_migrations_online())
