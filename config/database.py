# This file is for configuring your SQLAlchemy/Alembic database connection

from sqlalchemy import create_engine

from config.settings import SQL_ALCHEMY_URL

# Default setup is a postgresql database using asyncpg as the driver
engine = create_engine(SQL_ALCHEMY_URL)
