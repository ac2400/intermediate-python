from fastapi import FastAPI
from app.routes import habits
from contextlib import asynccontextmanager

# Import all models to ensure proper registration with SQLAlchemy
from app.models.db import engine, Base


# Function to initialize the database by creating all tables
async def init_db():
    async with engine.begin() as conn:
        # This creates all tables defined in your models if they don't exist
        await conn.run_sync(Base.metadata.create_all)


# Lifecycle manager for the FastAPI app
@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup: initialize database when the app starts
    await init_db()
    yield  # This is where the app runs
    # Shutdown: cleanup could go here when the app stops


# Create the FastAPI application with the lifespan manager
app = FastAPI(lifespan=lifespan)
# Include the habits router with the prefix "/habits"
app.include_router(habits.router, prefix="/habits", tags=["Habits"])


# Root endpoint that just returns a hello message
@app.get("/")
def read_root():
    return {"message": "Hello, world!"}
