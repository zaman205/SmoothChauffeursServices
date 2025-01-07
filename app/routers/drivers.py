
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database.database import get_db
from app.models.models import Driver, User

router = APIRouter(prefix="/drivers", tags=["drivers"])

@router.post("/signup")
def driver_signup(
    name: str,
    email: str,
    password: str,
    vehicle_make: str,
    vehicle_model: str,
    license_plate: str,
    vehicle_color: str,
    license_number: str,
    license_expiry_date: str,
    db: Session = Depends(get_db)
):
    if db.query(User).filter(User.email == email).first():
        raise HTTPException(status_code=400, detail="Email already registered")
    hashed_password = pwd_context.hash(password)
    new_user = User(name=name, email=email, hashed_password=hashed_password, role="driver")
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    new_driver = Driver(
        user_id=new_user.id,
        vehicle_make=vehicle_make,
        vehicle_model=vehicle_model,
        license_plate=license_plate,
        vehicle_color=vehicle_color,
        license_number=license_number,
        license_expiry_date=license_expiry_date
    )
    db.add(new_driver)
    db.commit()
    db.refresh(new_driver)
    return {"message": "Driver registered successfully", "driver_id": new_driver.id}

@router.get("/{driver_id}")
def get_driver_info(driver_id: int, db: Session = Depends(get_db)):
    driver = db.query(Driver).filter(Driver.id == driver_id).first()
    if not driver:
        raise HTTPException(status_code=404, detail="Driver not found")
    return {
        "driver_id": driver.id,
        "name": driver.user.name,
        "email": driver.user.email,
        "vehicle": {
            "make": driver.vehicle_make,
            "model": driver.vehicle_model,
            "license_plate": driver.license_plate,
            "color": driver.vehicle_color
        },
        "license": {
            "number": driver.license_number,
            "expiry_date": str(driver.license_expiry_date)
        }
    }
