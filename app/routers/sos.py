
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database.database import get_db
from app.models.models import Ride

router = APIRouter(prefix="/rides", tags=["sos"])

@router.post("/{ride_id}/sos")
def sos_alert(ride_id: int, user_id: int, message: str, db: Session = Depends(get_db)):
    ride = db.query(Ride).filter(Ride.id == ride_id).first()
    if not ride:
        raise HTTPException(status_code=404, detail="Ride not found")
    print(f"SOS Alert from user {user_id} during ride {ride_id}: {message}")
    return {"message": "SOS alert sent successfully"}
