from fastapi import APIRouter

from app.models.sheldra import ChatRequest, ChatResponse

router = APIRouter(prefix="/api/v1/sheldra", tags=["SHELDRA"])


@router.post("/chat", response_model=ChatResponse, summary="Send a message to SHELDRA")
async def chat(request: ChatRequest) -> ChatResponse:
    """Foundation stub; the Intelligence Engine replaces this in Phase 1."""
    return ChatResponse(
        response=f"SHELDRA received your message, {request.worker_id}.",
        confidence=0.0,
        trace_id=request.trace_id,
    )
