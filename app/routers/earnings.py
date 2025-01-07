
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.database import get_db
from app.models.models import Ride, Payment, RideStatus, PaymentStatus

router = APIRouter(prefix="/drivers", tags=["earnings"])

@router.get("/{driver_id}/earnings/report")
def driver_earnings_report(driver_id: int, db: Session = Depends(get_db)):
    completed_rides = db.query(Ride).filter(Ride.driver_id == driver_id, Ride.status == RideStatus.completed).all()
    total_earnings = sum(ride.payment.amount for ride in completed_rides if ride.payment.status == PaymentStatus.completed)
    report = [{"ride_id": ride.id, "earnings": ride.payment.amount} for ride in completed_rides]
    return {
        "driver_id": driver_id,
        "total_earnings": total_earnings,
        "rides": report
    }
