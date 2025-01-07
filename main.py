
from fastapi import FastAPI
from app.routers import auth, drivers, rides, payments
from app.database import database

app = FastAPI()

# Include routers
app.include_router(auth.router)
app.include_router(drivers.router)
app.include_router(rides.router)
app.include_router(payments.router)
