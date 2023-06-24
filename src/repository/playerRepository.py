from fastapi import WebSocket
from src.models.player import Player

from src.utils.generateUniqueIds import generateUniqueUserId


class InMemoryPlayerRepository:

    def __init__(self):
        self.players = {}

    def addPlayer(self, name: str, websocket: WebSocket):
        user_id = generateUniqueUserId()
        self.players[user_id] = Player(
            id=user_id, name=name, websocket=websocket)

    def getPlayers(self):
        return self.players.values()

    def getPlayerWebsockets(self):
        return [player.websocket for player in self.players.values()]

    def removePlayer(self, user_id: str):
        del self.players[user_id]
