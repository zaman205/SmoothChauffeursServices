
from fastapi import APIRouter, WebSocket, WebSocketDisconnect

router = APIRouter(prefix="/chat", tags=["chat"])

@router.websocket("/ws/{ride_id}")
async def chat_endpoint(ride_id: int, websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            data = await websocket.receive_text()
            print(f"Message for ride {ride_id}: {data}")
            await websocket.send_text(f"Received: {data}")
    except WebSocketDisconnect:
        print(f"Chat for ride {ride_id} disconnected")
