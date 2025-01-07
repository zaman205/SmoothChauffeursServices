
from fastapi import APIRouter

router = APIRouter(prefix="/safety", tags=["check_in"])

@router.post("/checkin")
def check_in_safety(passenger_id: int, ride_id: int, contact_email: str):
    # Simulate sending a notification to a trusted contact
    return {"message": f"Safety check-in notification sent to {contact_email} for passenger {passenger_id}."}
