from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from app.manager import ConnectionManager

app = FastAPI()
manager = ConnectionManager()

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await manager.connect(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            await manager.broadcast(f"Echo: {data}")
    except WebSocketDisconnect:
        await manager.broadcast("Connection closed")
        manager.disconnect(websocket)
