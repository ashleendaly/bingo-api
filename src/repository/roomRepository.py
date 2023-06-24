from src.models.room import Room
from src.models.event import EventList
from fastapi import WebSocket


class InMemoryRoomRepository:

    def __init__(self):
        self.rooms = {}

    def createRoom(self, code: str, creator_id: str):
        self.rooms[code] = Room(code=code, creatorId=creator_id)
        self.rooms[code].usersJoined.add(creator_id)
        print(self.rooms)
        return code

    def joinRoom(self, code: str, user_id: str):
        self.rooms[code].usersJoined.add(user_id)
        print(self.rooms)

    def setEventList(self, code: str, eventList: EventList):
        self.rooms[code].eventList = eventList

    def getEventList(self, code: str):
        return self.rooms[code].eventList

    def roomExists(self, code: str):
        if code in list(self.rooms.keys()):
            return True
        else:
            return False

    def userInRoom(self, code: str, user_id: str):
        if user_id in self.rooms[code].usersJoined:
            return True
        else:
            return False

    def addWebSocketToRoom(self, code: str, websocket: WebSocket):
        self.rooms[code].websocketConnecions.add(websocket)

    def getAllWebSocketsInRoom(self, code: str):
        return self.rooms[code].websocketConnecions

    def removeWebSocketFromRoom(self, code: str, websocket: WebSocket):
        self.rooms[code].websocketConnecions.remove(websocket)


class DatabaseRoomRepository:
    # TODO: Implement database repository

    def __init__(self, db_url: str):
        # Initialize database connection
        pass

    def createRoom(self, code: str, creator_id: str):
        pass

    def joinRoom(self, code: str, user_id: str):
        pass

    def setEventList(self, code: str, eventList: EventList):
        pass

    def getEventList(self, code: str):
        pass

    def roomExists(self, code: str):
        pass

    def userInRoom(self, code: str, user_id: str):
        pass

    def addWebSocketToRoom(self, code: str, websocket: WebSocket):
        pass

    def getAllWebSocketsInRoom(self, code: str):
        pass

    def removeWebSocketFromRoom(self, code: str, websocket: WebSocket):
        pass
