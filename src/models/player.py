from typing import Optional
from fastapi import WebSocket
from pydantic import BaseModel


class Player(BaseModel):
    id: str
    name: str
    websocket: Optional[WebSocket]
