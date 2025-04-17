from sqlalchemy import ForeignKey, Date
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.models.db import Base
from datetime import date as date_type
from typing import TYPE_CHECKING

# Prevent circular imports (only for type checking)
if TYPE_CHECKING:
    from app.models.habit import Habit


# Database model for habit completion records
class HabitCompletion(Base):
    __tablename__ = "habit_completions"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    # Foreign key points to the habits table's id column
    # ondelete="CASCADE" means if a habit is deleted, all its completions are deleted too
    habit_id: Mapped[int] = mapped_column(ForeignKey("habits.id", ondelete="CASCADE"))
    date: Mapped[date_type] = mapped_column(
        Date
    )  # Stores the date when habit was completed

    # Relationship back to the Habit model
    # This lets you access the parent habit from a completion record
    habit: Mapped["Habit"] = relationship("Habit", back_populates="completions")
