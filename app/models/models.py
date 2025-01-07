
from sqlalchemy import Column, Integer, String, ForeignKey, Date, Float, Enum, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
import enum
from app.database.database import Base

class RideStatus(enum.Enum):
    pending = "pending"
    accepted = "accepted"
    completed = "completed"
    canceled = "canceled"

class PaymentStatus(enum.Enum):
    pending = "pending"
    completed = "completed"
    failed = "failed"

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    role = Column(String, nullable=False)

class Driver(Base):
    __tablename__ = "drivers"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    vehicle_make = Column(String, nullable=False)
    vehicle_model = Column(String, nullable=False)
    license_plate = Column(String, nullable=False)
    vehicle_color = Column(String, nullable=True)
    license_number = Column(String, nullable=False)
    license_expiry_date = Column(Date, nullable=False)
    user = relationship("User", back_populates="driver_profile")

class Ride(Base):
    __tablename__ = "rides"
    id = Column(Integer, primary_key=True, index=True)
    passenger_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    driver_id = Column(Integer, ForeignKey("users.id"), nullable=True)
    pickup_location = Column(String, nullable=False)
    dropoff_location = Column(String, nullable=False)
    status = Column(Enum(RideStatus), default=RideStatus.pending, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

class Payment(Base):
    __tablename__ = "payments"
    id = Column(Integer, primary_key=True, index=True)
    ride_id = Column(Integer, ForeignKey("rides.id"), nullable=False)
    amount = Column(Float, nullable=False)
    status = Column(Enum(PaymentStatus), default=PaymentStatus.pending, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
