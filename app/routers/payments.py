
import stripe
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database.database import get_db
from app.models.models import Payment, PaymentStatus

router = APIRouter(prefix="/payments", tags=["payments"])

stripe.api_key = "your_stripe_secret_key"

@router.post("/create")
def create_payment(ride_id: int, amount: float, db: Session = Depends(get_db)):
    payment = Payment(
        ride_id=ride_id,
        amount=amount,
        status=PaymentStatus.pending
    )
    db.add(payment)
    db.commit()
    db.refresh(payment)
    return {"payment_id": payment.id, "status": payment.status}

@router.post("/confirm")
def confirm_payment(payment_id: int, db: Session = Depends(get_db)):
    payment = db.query(Payment).filter(Payment.id == payment_id).first()
    if not payment or payment.status != PaymentStatus.pending:
        raise HTTPException(status_code=400, detail="Payment not valid for confirmation")
    payment.status = PaymentStatus.completed
    db.commit()
    return {"message": "Payment confirmed", "payment_id": payment.id}
