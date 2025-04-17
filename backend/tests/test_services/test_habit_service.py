import pytest
import pytest_asyncio
from unittest.mock import patch

from app.models.habit import Habit
from app.services.habit_service import get_all_habits


# Patched version of create_habit that uses our test database
@pytest_asyncio.fixture
async def patched_create_habit(test_db):
    async def _create_habit(name: str, frequency: str):
        # Create a new Habit object
        new_habit = Habit(name=name, frequency=frequency)
        # Add to test session
        test_db.add(new_habit)
        # Commit the transaction
        await test_db.commit()
        # Refresh to get generated values
        await test_db.refresh(new_habit)
        return new_habit

    # Use patch to replace the AsyncSessionLocal in the service
    with patch("app.services.habit_service.AsyncSessionLocal") as mock_session:
        # Configure the mock to return our test_db when used as context manager
        mock_session.return_value.__aenter__.return_value = test_db
        yield _create_habit


# Test creating a habit with isolated test database
@pytest.mark.asyncio
async def test_create_habit_isolated(patched_create_habit):
    # Test data
    name = "Meditation"
    frequency = "daily"

    # Call the patched service function
    new_habit = await patched_create_habit(name, frequency)

    # Assertions
    assert new_habit is not None
    assert new_habit.id is not None
    assert new_habit.name == name
    assert new_habit.frequency == frequency
    assert new_habit.streak == 0


# Test getting all habits with isolated test database
@pytest.mark.asyncio
async def test_get_all_habits_isolated(test_db, test_habit):
    # Add a second habit to make the test more robust
    second_habit = Habit(name="Reading", frequency="daily")
    test_db.add(second_habit)
    await test_db.commit()

    # Patch the AsyncSessionLocal to use our test database
    with patch("app.services.habit_service.AsyncSessionLocal") as mock_session:
        mock_session.return_value.__aenter__.return_value = test_db

        # Call the service function
        habits = await get_all_habits()

        # Verify we got at least two habits
        assert len(habits) >= 2
        habit_names = [h.name for h in habits]
        assert test_habit.name in habit_names
        assert "Reading" in habit_names
