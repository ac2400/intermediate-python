from fastapi import APIRouter
from app.models.schemas import HabitCreate
from app.services import habit_service

# Create a router for habit-related endpoints
router = APIRouter()


# GET endpoint at /habits/ that returns all habits
@router.get("/")
async def get_habits():
    # Call the service function to get habits from the database
    return await habit_service.get_all_habits()


# POST endpoint at /habits/ that creates a new habit
@router.post("/")
async def create_habit(payload: HabitCreate):
    # Extract data from the request and call the service function
    await habit_service.create_habit(payload.name, payload.frequency)
    # Return a success message
    return {"message": f"Habit '{payload.name}' created."}
