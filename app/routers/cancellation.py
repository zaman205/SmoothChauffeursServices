
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database.database import get_db
from app.models.models import Ride, RideStatus

router = APIRouter(prefix="/rides", tags=["cancellation"])

@router.post("/{ride_id}/cancel")
def cancel_ride(ride_id: int, user_id: int, reason: str, db: Session = Depends(get_db)):
    ride = db.query(Ride).filter(Ride.id == ride_id).first()
    if not ride:
        raise HTTPException(status_code=404, detail="Ride not found")
    ride.status = RideStatus.canceled
    ride.cancellation_reason = reason
    db.commit()
    return {"message": "Ride canceled successfully", "reason": reason}
