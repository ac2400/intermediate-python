# Import all models to ensure they are registered with SQLAlchemy
from app.models.db import Base
from app.models.habit import Habit
from app.models.habit_completion import HabitCompletion

# This ensures all models are properly loaded and registered
__all__ = ["Base", "Habit", "HabitCompletion"]
