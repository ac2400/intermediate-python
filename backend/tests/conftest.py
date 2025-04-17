# tests/conftest.py
import pytest
import pytest_asyncio
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.pool import StaticPool
from typing import Dict, Any

from app.models.db import Base
from app.models.habit import Habit
from app.main import app
from fastapi.testclient import TestClient

# Test database URL - use a file-based database for simplicity
TEST_DATABASE_URL = "sqlite+aiosqlite:///:memory:"


# Create a single engine instance that will be reused across tests
@pytest_asyncio.fixture(scope="session")
async def test_engine():
    engine = create_async_engine(
        TEST_DATABASE_URL,
        connect_args={"check_same_thread": False},
        poolclass=StaticPool,  # Use StaticPool to maintain a single connection
        echo=True,
    )

    # Create all tables
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    yield engine

    # Drop all tables after tests
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)


# Session factory - create once per session
@pytest_asyncio.fixture(scope="session")
async def session_factory(test_engine):
    return async_sessionmaker(
        bind=test_engine,
        class_=AsyncSession,
        expire_on_commit=False,
    )


# Session fixture - provides fresh db session for each test
@pytest_asyncio.fixture
async def test_db(session_factory):
    async with session_factory() as session:
        yield session
        await session.rollback()  # Roll back changes after each test


# Sample data fixture
@pytest.fixture
def sample_habit_data() -> Dict[str, Any]:
    return {"name": "Exercise", "frequency": "daily"}


# Fixture that creates a test habit in the database
@pytest_asyncio.fixture
async def test_habit(test_db, sample_habit_data) -> Habit:
    habit = Habit(**sample_habit_data)
    test_db.add(habit)
    await test_db.commit()
    await test_db.refresh(habit)
    return habit


# FastAPI test client
@pytest.fixture
def client():
    return TestClient(app)
