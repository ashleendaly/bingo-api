from typing import List
from pydantic import BaseModel

from models.incident import Incident


class Room(BaseModel):
    id: str
    incidentList: List(Incident) = []
    websocketConnecions: set = set()
