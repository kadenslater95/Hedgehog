
from sqlalchemy import create_engine

from config.init import ENV

engine = create_engine(f"postgresql+asyncpg://{ENV['DB_USERNAME']}:{ENV['DB_PASSWORD']}")
