# This file is for configuring your SQLAlchemy/Alembic database connection

from sqlalchemy import create_engine

from config.settings import ENV

# Default setup is a postgresql database using asyncpg as the driver
engine = create_engine(f"postgresql+asyncpg://{ENV['DB_USERNAME']}:{ENV['DB_PASSWORD']}@localhost:5432/{ENV['DB_DATABASENAME']}")
