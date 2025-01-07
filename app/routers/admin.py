
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.database import get_db
from app.models.models import Ride, User, Payment, PaymentStatus

router = APIRouter(prefix="/admin", tags=["admin"])

@router.get("/overview")
def admin_overview(db: Session = Depends(get_db)):
    total_rides = db.query(Ride).count()
    total_users = db.query(User).count()
    total_payments = db.query(Payment).filter(Payment.status == PaymentStatus.completed).count()
    total_earnings = db.query(Payment).filter(Payment.status == PaymentStatus.completed).all()
    return {
        "total_rides": total_rides,
        "total_users": total_users,
        "total_completed_payments": total_payments,
        "total_earnings": sum(p.amount for p in total_earnings)
    }
