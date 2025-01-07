
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.database import get_db
from app.models.models import Rating

router = APIRouter(prefix="/ratings", tags=["ratings"])

@router.post("/add")
def add_rating(ride_id: int, user_id: int, rating: float, review: str = None, db: Session = Depends(get_db)):
    new_rating = Rating(ride_id=ride_id, user_id=user_id, rating=rating, review=review)
    db.add(new_rating)
    db.commit()
    db.refresh(new_rating)
    return {"message": "Rating added successfully", "rating_id": new_rating.id}

@router.get("/{user_id}")
def get_ratings(user_id: int, db: Session = Depends(get_db)):
    ratings = db.query(Rating).filter(Rating.user_id == user_id).all()
    return ratings
