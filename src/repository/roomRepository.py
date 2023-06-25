from fastapi import WebSocket
from src.models.player import Player
from src.models.incident import Incident
from src.models.room import Room
from src.utils.generateBingoCard import generateBingoCard
from src.utils.generateUniqueIds import generateUniqueUserId


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

    def getIncidentList(self, code: str):
        return self.getIncidentList()

    def getGamePhase(self, code: str):
        return self.rooms[code].game.phase

    def getPlayerList(self, code: str):
        return self.rooms[code].game.players

    def addPlayer(self, code: str, name: str, websocket: WebSocket):
        user_id = generateUniqueUserId()
        self.rooms[code].game.players.append(Player(
            id=user_id, name=name, websocket=websocket))

    def getPlayerWebsockets(self, code: str):
        return [player.websocket for player in self.rooms[code].game.players]

    def removePlayer(self, user_id: str, code: str):
        pass

    def generateHandshake(self, code: str):
        return {"type": "handshake", "players": self.getPlayerList(), "incidents": self.getIncidentList(), "code": code}

    def gameStart(self, code: str):
        self.rooms[code].game.phase = "play"

    def gameEnd(self, code: str):
        self.rooms[code].game.phase = "lobby"

    def gameWon(self, code: str):
        self.rooms[code].game.phase = "lobby"

    def handleLobbyWsEvent(self, event, code: str):

        if event["type"] == "startGame":
            self.gameStart(code)
            return generateBingoCard(self.incidents.getIncidents(), 14)

        elif event["type"] == "addIncident":
            self.rooms[code].incidentList.append(Incident(
                id=event["id"], name=event["name"], count=0))

        elif event["type"] == "removeIncident":
            self.rooms[code].incidentList.remove(Incident(
                id=event["id"], name=event["name"], count=0))

        else:
            raise Exception("Invalid event type")

        return self.generateHandshake()

    def handlePlayWsEvent(self, event, code: str):

        if event["type"] == "endGame":
            self.gameEnd(code)

        elif event["type"] == "winGame":
            self.gameWon(code)

        elif event["type"] == "incidentOccured":
            self.incidents.incidentOccured(Incident(
                id=event["id"], name=event["name"], count=0))

        else:
            raise Exception("Invalid event type")

        return self.generateHandshake()


class DatabaseRoomRepository:
    # TODO: Implement database repository

    def __init__(self, db_url: str):
        # Initialize database connection
        pass

    def createRoom(self, code: str):
        pass

    def roomExists(self, code: str):
        pass
