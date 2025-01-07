
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.database import get_db
from app.models.models import PreferredDriver

router = APIRouter(prefix="/passengers", tags=["preferred_drivers"])

@router.post("/{passenger_id}/favorite-driver")
def favorite_driver(passenger_id: int, driver_id: int, db: Session = Depends(get_db)):
    preferred_driver = PreferredDriver(passenger_id=passenger_id, driver_id=driver_id)
    db.add(preferred_driver)
    db.commit()
    return {"message": "Driver added to favorites"}
