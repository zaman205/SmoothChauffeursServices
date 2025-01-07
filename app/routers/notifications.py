
from fastapi import APIRouter, WebSocket, WebSocketDisconnect
import asyncio

router = APIRouter(prefix="/notifications", tags=["notifications"])

@router.websocket("/driver/{driver_id}")
async def driver_notifications(driver_id: int, websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            notification = f"New ride request for driver {driver_id}"
            await websocket.send_text(notification)
            await asyncio.sleep(5)
    except WebSocketDisconnect:
        print(f"Driver {driver_id} disconnected")

@router.websocket("/passenger/{passenger_id}")
async def passenger_notifications(passenger_id: int, websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            notification = f"Driver is nearby for passenger {passenger_id}"
            await websocket.send_text(notification)
            await asyncio.sleep(5)
    except WebSocketDisconnect:
        print(f"Passenger {passenger_id} disconnected")
