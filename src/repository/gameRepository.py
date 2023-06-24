from fastapi import WebSocket
from src.models.incident import Incident
from src.models.player import Player
from src.utils.generateBingoCard import generateBingoCard
from src.repository.instance import incidentRepository, playerRepository


class InMemoryGameRepository:

    def __init__(self, roomCode: str):
        self.players = playerRepository
        self.incidents = incidentRepository
        self.roomCode = roomCode
        self.phase = "lobby"

    def generateHandshake(self):
        return {"type": "handshake", "players": self.players.getPlayers, "incidents": self.incidents.getIncidents, "code": self.roomCode}

    def gameStart(self):
        self.phase = "play"

    def gameEnd(self):
        self.phase = "lobby"

    def gameWon(self):
        self.phase = "lobby"

    def handleLobbyWsEvent(self, event):
        if event["type"] == "startGame":
            self.gameStart()
            return generateBingoCard(self.incidents.getIncidents(), 14)
        elif event["type"] == "addIncident":
            self.incidents.addIncident(Incident(
                id=event["id"], name=event["name"], count=0))
        elif event["type"] == "removeIncident":
            self.incidents.removeIncident(Incident(
                id=event["id"], name=event["name"], count=0))
        else:
            raise Exception("Invalid event type")
        return self.generateHandshake()

    def handlePlayWsEvent(self, event):
        if event["type"] == "endGame":
            self.gameEnd()
        elif event["type"] == "winGame":
            self.gameWon()
        elif event["type"] == "incidentOccured":
            self.incidents.incidentOccured(Incident(
                id=event["id"], name=event["name"], count=0))
        else:
            raise Exception("Invalid event type")
        return self.generateHandshake()
