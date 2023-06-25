from typing import List
from pydantic import BaseModel

from src.models.incident import Incident
from src.models.player import Player


class Game(BaseModel):
    phase: str = "lobby"
    players: List


class Room(BaseModel):
    code: str
    incidentList: List
    game: Game
    websocketConnecions: set = set()
