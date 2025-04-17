from pydantic import BaseModel
from datetime import date
from typing import List


# This defines the shape of habit data returned by the API
class HabitResponse(BaseModel):
    id: int
    name: str
    frequency: str
    streak: int
    dates_completed: List[date]


# This defines the shape of data needed to create a new habit
# Only requires name and frequency - the rest have defaults or are generated
class HabitCreate(BaseModel):
    name: str
    frequency: str


# Configuration for Pydantic models
class Config:
    # Enables ORM mode - allows conversion from SQLAlchemy models to Pydantic models
    from_attributes = True
