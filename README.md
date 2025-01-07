
# Ride Share App

This is a Ride Share Application backend built with **FastAPI**. It includes functionalities for passenger and driver registration, ride booking, real-time updates, and payment processing.

## Features

- **User Authentication**:
  - Signup and login for passengers and drivers.
- **Driver Management**:
  - Driver registration with vehicle and license details.
- **Ride Booking**:
  - Passengers can book rides with pickup and dropoff locations.
  - Drivers can accept and complete rides.
- **Payment Processing**:
  - Payment integration using Stripe.
  - Track payment status and driver earnings.

## Project Structure

```
ride_share_app/
├── main.py                  # Entry point for the application
├── app/
│   ├── database/
│   │   └── database.py      # Database connection and session management
│   ├── models/
│   │   └── models.py        # Database models for Users, Drivers, Rides, and Payments
│   ├── routers/
│       ├── auth.py          # Authentication endpoints
│       ├── drivers.py       # Driver-related endpoints
│       ├── rides.py         # Ride-related endpoints
│       └── payments.py      # Payment-related endpoints
```

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/ride-share-app.git
   cd ride-share-app
   ```

2. Create a virtual environment and install dependencies:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   uvicorn main:app --reload
   ```

4. Access the API docs at:
   - Swagger: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
   - ReDoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

## API Endpoints

### Authentication
- `POST /auth/signup`: User registration.
- `POST /auth/login`: User login.

### Drivers
- `POST /drivers/signup`: Register a driver with vehicle and license details.
- `GET /drivers/{driver_id}`: Retrieve driver and vehicle information.

### Rides
- `POST /rides/book`: Book a ride as a passenger.
- `PUT /rides/{ride_id}/complete`: Mark a ride as completed.

### Payments
- `POST /payments/create`: Create a payment for a ride.
- `POST /payments/confirm`: Confirm payment.

## Requirements

- Python 3.8+
- FastAPI
- SQLAlchemy
- SQLite (default database)
- Stripe Python SDK

## License

This project is licensed under the MIT License.
