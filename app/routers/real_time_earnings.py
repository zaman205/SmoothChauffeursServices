
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.database import get_db
from app.models.models import Ride, Payment, PaymentStatus, RideStatus

router = APIRouter(prefix="/earnings", tags=["real_time_earnings"])

@router.get("/{driver_id}/daily")
def real_time_earnings(driver_id: int, db: Session = Depends(get_db)):
    completed_rides = db.query(Ride).filter(Ride.driver_id == driver_id, Ride.status == RideStatus.completed).all()
    daily_earnings = sum(ride.payment.amount for ride in completed_rides if ride.payment.status == PaymentStatus.completed)
    return {"driver_id": driver_id, "daily_earnings": daily_earnings}
