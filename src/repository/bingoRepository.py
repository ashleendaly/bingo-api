import uuid
from src.models.bingo import EventList


class InMemoryBingoRepository:

    def __init__(self):
        self.eventLists = {}

    def addEventList(self, eventList: EventList):
        self.eventLists[eventList.id] = eventList
        print(self.eventLists)

    def getEventList(self, id):
        return self.eventLists[id]


class DatabaseBingoRepository:
    # TODO: Implement database repository

    def __init__(self, db_url: str):
        # Initialize database connection
        pass

    def addEventList(self, eventList: EventList):
        pass

    def getEventList(self, id):
        pass
