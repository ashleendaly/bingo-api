from typing import List
import uuid
from pydantic import BaseModel


class Event(BaseModel):
    id: int
    label: str
    hasHappened: bool = False


class EventList(BaseModel):
    id: str = uuid.uuid4()
    events: List[Event] = []
