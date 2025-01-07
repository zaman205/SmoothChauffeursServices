
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_signup():
    response = client.post("/auth/signup", json={
        "name": "John Doe",
        "email": "test@example.com",
        "password": "securepassword",
        "role": "passenger"
    })
    assert response.status_code == 201
    assert response.json()["message"] == "User created successfully"
