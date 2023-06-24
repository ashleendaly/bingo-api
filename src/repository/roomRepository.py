from typing import List
from models.incident import Incident
from src.models.room import Room
from fastapi import WebSocket


class InMemoryRoomRepository:

    def __init__(self):
        self.rooms = {}

    def createRoom(self, code: str):
        self.rooms[code] = Room(code=code)
        print(self.rooms)
        return code

    def roomExists(self, code: str):
        if code in list(self.rooms.keys()):
            return True
        else:
            return False


class DatabaseRoomRepository:
    # TODO: Implement database repository

    def __init__(self, db_url: str):
        # Initialize database connection
        pass

    def createRoom(self, code: str):
        pass

    def roomExists(self, code: str):
        pass
