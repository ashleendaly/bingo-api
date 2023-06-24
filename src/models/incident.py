from typing import List
import uuid
from pydantic import BaseModel


class Incident(BaseModel):
    id: str = str(uuid.uuid4())
    label: str
    count: int = 0
