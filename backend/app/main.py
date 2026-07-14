from contextlib import asynccontextmanager

from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware

from app.api.routes import router
from app.api.websocket import ws_manager
from app.core.config import get_settings
from app.services.redis import redis_manager


@asynccontextmanager
async def lifespan(_: FastAPI):
    try:
        await redis_manager.connect()
    except Exception:
        # Redis is optional while running the API skeleton in isolation.
        pass
    yield
    await redis_manager.disconnect()


settings = get_settings()
app = FastAPI(title="SHELDRA API", version="0.1.0", lifespan=lifespan)
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(router)


@app.get("/health", tags=["System"])
async def health() -> dict[str, str]:
    return {"status": "ok", "service": "sheldra-api"}


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket) -> None:
    await ws_manager.connect(websocket)
    try:
        await websocket.send_json({"type": "connected", "data": {"service": "SHELDRA"}})
        while True:
            message = await websocket.receive_json()
            await websocket.send_json({"type": "chat", "data": message})
    except WebSocketDisconnect:
        ws_manager.disconnect(websocket)
