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

## Troubleshooting

If you encounter issues while setting up or running the application, refer to the following steps:

### 1. **ModuleNotFoundError**

- If you see an error like `ModuleNotFoundError: No module named 'passlib'`, install the missing module:
  ```bash
  pip install "passlib[bcrypt]"
  ```
- For `jose` library issues, install:
  ```bash
  pip install python-jose
  ```
- For `stripe` module issues, install:
  ```bash
  pip install stripe
  ```

### 2. **Root Endpoint (`/`) Not Found**

If visiting `http://127.0.0.1:8000/` gives a `404 Not Found` error, add a root route in `main.py`:
```python
@app.get("/")
def read_root():
    return {"message": "Welcome to the Ride Share App!"}
```

### 3. **Browser Favicon Warnings**

Browsers often request a `favicon.ico`, leading to warnings. Add a placeholder route:
```python
@app.get("/favicon.ico")
def favicon():
    return {"message": "Favicon not available"}
```

### 4. **Port Issues**

If the default port (`8000`) is in use, specify a different port:
```bash
uvicorn main:app --host 127.0.0.1 --port 8080 --reload
```

### 5. **Database Troubleshooting**

If the SQLite database is not being created or updated:
- Check the database file (`ride_share_app.db`) in the project directory.
- Use `sqlite3` to inspect the database:
  ```bash
  sqlite3 ride_share_app.db
  .tables
  SELECT * FROM users;
  ```

### 6. **General Dependency Issues**

Ensure all dependencies are installed:
```bash
pip install -r requirements.txt
```

If new dependencies are added, update `requirements.txt`:
```bash
pip freeze > requirements.txt
```

### 7. **Debugging Tips**

- Always check error logs in the terminal for details.
- Clear your browser cache if changes don't reflect immediately.
- Restart the application after making code changes:
  ```bash
  uvicorn main:app --reload
  ```

If you encounter further issues, share the specific error logs for assistance.
