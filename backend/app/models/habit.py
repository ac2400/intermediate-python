from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.models.db import Base
from typing import TYPE_CHECKING, List

# This conditional import prevents circular imports
# It's only used by the type checker, not at runtime
if TYPE_CHECKING:
    from app.models.habit_completion import HabitCompletion


# This is your database model for habits - it maps to a database table
class Habit(Base):
    """
    This is the model for habits.
    """

    # Define the table name in the database
    __tablename__ = "habits"

    # Define columns with their types and constraints
    # Mapped[type] is SQLAlchemy's way of defining column types with Python type hints
    id: Mapped[int] = mapped_column(
        primary_key=True, index=True
    )  # Primary key, auto-incremented
    name: Mapped[str] = mapped_column(String, nullable=False)  # Required field
    frequency: Mapped[str] = mapped_column(String, nullable=False)  # Required field
    streak: Mapped[int] = mapped_column(Integer, default=0)  # Default value of 0

    # Define a relationship to HabitCompletion records
    # This creates a virtual field that lets you access related records
    # back_populates="habit" creates a two-way relationship
    # cascade="all, delete-orphan" means when a habit is deleted, its completions are too
    completions: Mapped[List["HabitCompletion"]] = relationship(
        "HabitCompletion", back_populates="habit", cascade="all, delete-orphan"
    )
