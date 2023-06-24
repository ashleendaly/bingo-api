from pydantic import BaseModel

from src.models.event import EventList


class Room(BaseModel):
    code: str
    usersJoined: set = set()
    eventList: EventList = []
    creatorId: str
    websocketConnecions: set = set()
