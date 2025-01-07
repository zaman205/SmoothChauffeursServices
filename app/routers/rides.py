
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database.database import get_db
from app.models.models import Ride, RideStatus

router = APIRouter(prefix="/rides", tags=["rides"])

@router.post("/book")
def book_ride(passenger_id: int, pickup_location: str, dropoff_location: str, db: Session = Depends(get_db)):
    new_ride = Ride(
        passenger_id=passenger_id,
        pickup_location=pickup_location,
        dropoff_location=dropoff_location
    )
    db.add(new_ride)
    db.commit()
    db.refresh(new_ride)
    return {"ride_id": new_ride.id, "status": new_ride.status}

@router.put("/{ride_id}/complete")
def complete_ride(ride_id: int, db: Session = Depends(get_db)):
    ride = db.query(Ride).filter(Ride.id == ride_id).first()
    if not ride or ride.status != RideStatus.accepted:
        raise HTTPException(status_code=400, detail="Ride not eligible for completion")
    ride.status = RideStatus.completed
    db.commit()
    return {"message": "Ride completed", "ride_id": ride.id}
