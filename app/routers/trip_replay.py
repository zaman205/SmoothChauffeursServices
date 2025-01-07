
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.database import get_db
from app.models.models import Ride

router = APIRouter(prefix="/rides", tags=["trip_replay"])

@router.get("/{ride_id}/replay")
def trip_replay(ride_id: int, db: Session = Depends(get_db)):
    ride = db.query(Ride).filter(Ride.id == ride_id).first()
    if not ride:
        return {"message": "Ride not found"}
    return {
        "route": {"pickup": ride.pickup_location, "dropoff": ride.dropoff_location},
        "fare": ride.payment.amount
    }
