from typing import List
import uuid
from pydantic import BaseModel


class Event(BaseModel):
    id: int
    label: str
    count: int = 0

class EventList(BaseModel):
    """required for fastAPI"""
    events: List[Event] = []
