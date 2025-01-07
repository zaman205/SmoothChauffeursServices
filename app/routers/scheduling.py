
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database.database import get_db
from app.models.models import Ride

router = APIRouter(prefix="/rides", tags=["scheduling"])

@router.post("/schedule")
def schedule_ride(
    passenger_id: int, pickup_location: str, dropoff_location: str, scheduled_time: str, db: Session = Depends(get_db)
):
    new_ride = Ride(
        passenger_id=passenger_id,
        pickup_location=pickup_location,
        dropoff_location=dropoff_location,
        scheduled_time=scheduled_time
    )
    db.add(new_ride)
    db.commit()
    return {"message": "Ride scheduled successfully", "ride_id": new_ride.id}
