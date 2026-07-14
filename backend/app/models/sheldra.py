from __future__ import annotations

from datetime import datetime
from typing import Any, Dict, List, Literal, Optional
from uuid import UUID, uuid4

from pydantic import BaseModel, Field


class ChatContext(BaseModel):
    zone_id: Optional[str] = None
    equipment_id: Optional[str] = None
    active_hazard: Optional[str] = None
    metadata: Dict[str, Any] = Field(default_factory=dict)


class ChatRequest(BaseModel):
    worker_id: str = Field(min_length=1, max_length=128)
    message: str = Field(min_length=1, max_length=4_000)
    context: ChatContext = Field(default_factory=ChatContext)
    trace_id: UUID = Field(default_factory=uuid4)


class AvatarCommand(BaseModel):
    gesture: Literal["idle", "nod", "point", "warning"] = "idle"
    tone: Literal["calm", "normal", "urgent", "praise"] = "normal"


class Citation(BaseModel):
    document: str
    section: Optional[str] = None
    page: Optional[int] = Field(default=None, ge=1)


class ChatResponse(BaseModel):
    response: str
    avatar_command: AvatarCommand = Field(default_factory=AvatarCommand)
    confidence: float = Field(ge=0, le=1)
    trace_id: UUID
    citations: List[Citation] = Field(default_factory=list)
    timestamp: datetime = Field(default_factory=datetime.utcnow)


class StreamMessage(BaseModel):
    type: Literal["connected", "chat", "error", "heartbeat"]
    data: Dict[str, Any] = Field(default_factory=dict)
