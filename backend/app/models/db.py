from dotenv import load_dotenv
import os
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase

# Load environment variables from a .env file
load_dotenv()

# Get the database connection string from environment variables
DATABASE_URL = os.getenv("DATABASE_URL")
if not DATABASE_URL:
    raise ValueError("DATABASE_URL environment variable is not set")

# Create an async engine - this establishes the connection to your database
# echo=True means SQL commands will be printed to the console (helpful for debugging)
engine = create_async_engine(DATABASE_URL, echo=True)

# Create a session factory that will let you interact with the database
# expire_on_commit=False means you can still access model attributes after committing
AsyncSessionLocal = async_sessionmaker(engine, expire_on_commit=False)


# Base class for all your models - all database models will inherit from this
class Base(DeclarativeBase):
    pass
