from fastapi import APIRouter, HTTPException, WebSocket
from src.utils.generateUniqueIds import generateUniqueRoomCode, generateUniqueUserId
from src.repository.instance import roomRepository, gameRepository

router = APIRouter()


@router.websocket("/create/", summmary="Create a room and connect to it")
async def createAndConnect(websocket: WebSocket, name: str):

    await websocket.accept()

    roomCode = generateUniqueRoomCode()
    roomRepository.createRoom(roomCode)

    try:
        gameRepository.players.addPlayer(name, websocket)
        await websocket.send_json(gameRepository.generateHandshake())

        while True:
            event = await websocket.recieve_json()
            if gameRepository.phase == "lobby":
                message = gameRepository.handleLobbyWsEvent(event)
                for player in gameRepository.players.getPlayers():
                    await player.websocket.send_json(message)

            if gameRepository.phase == "play":
                message = gameRepository.handlePlayWsEvent(event)
                for player in gameRepository.players.getPlayers():
                    await player.websocket.send_json(message)

    except WebSocket.exceptions.ConnectionClosedError:
        Exception("Connection closed")


@router.websocket("/join/{roomCode}/{name}", summary="Join a room and connect to it")
async def joinAndConnect(websocket: WebSocket, roomCode: str, name: str):
    if not roomRepository.roomExists(roomCode):
        raise HTTPException(status_code=404, detail="Room not found")

    await websocket.accept()

    try:
        gameRepository.players.addPlayer(name, websocket)
        await websocket.send_json(gameRepository.generateHandshake())

        while True:
            event = await websocket.recieve_json()
            if gameRepository.phase == "lobby":
                handshake = gameRepository.handleLobbyWsEvent(event)
                await websocket.send_json(handshake)

            if gameRepository.phase == "play":
                handshake = gameRepository.handlePlayWsEvent(event)
                await websocket.send_json(handshake)

    except WebSocket.exceptions.ConnectionClosedError:
        Exception("Connection closed")
