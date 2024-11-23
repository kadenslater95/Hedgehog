# This file is for storing global variables and "contants" (python doesn't check reassignment)

from dotenv import dotenv_values

ENV = dotenv_values(".env.local")

SQL_ALCHEMY_URL = f"postgresql+asyncpg://{ENV['DB_USERNAME']}:{ENV['DB_PASSWORD']}@localhost:5432/{ENV['DB_DATABASENAME']}"
