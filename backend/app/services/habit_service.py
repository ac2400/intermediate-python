from sqlalchemy.future import select
from app.models.db import AsyncSessionLocal
from app.models.habit import Habit
from typing import Sequence


async def create_habit(name: str, frequency: str) -> Habit:
    """
    Creates a new habit in the database
    """
    # Create a database session (connection) using a context manager
    # When the context manager exits, the session is closed automatically
    async with AsyncSessionLocal() as session:
        # Create a new Habit object (not yet in the database)
        new_habit = Habit(name=name, frequency=frequency)
        # Add the new habit to the session (preparing it to be saved)
        session.add(new_habit)
        # Commit the changes to the database (this actually saves it)
        await session.commit()
        # Refresh the habit object with any database-generated values
        await session.refresh(new_habit)
        # Return the newly created habit
        return new_habit


# Get all habits from the database
async def get_all_habits() -> Sequence[Habit]:
    async with AsyncSessionLocal() as session:
        # Create a SELECT query using SQLAlchemy
        # select(Habit) is like "SELECT * FROM habits" in SQL
        result = await session.execute(select(Habit))
        # Convert the result to a list of Habit objects and return it
        return result.scalars().all()
