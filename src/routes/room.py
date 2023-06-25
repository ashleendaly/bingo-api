from fastapi import APIRouter, HTTPException, WebSocket
from src.utils.generateUniqueIds import generateUniqueRoomCode
from src.repository.instance import roomRepository

router = APIRouter()


@router.websocket("/create/")
async def createAndConnect(websocket: WebSocket, name: str):

    await websocket.accept()

    roomCode = generateUniqueRoomCode()
    roomRepository.createRoom(roomCode)

    roomRepository.addPlayer(roomCode, name, websocket)
    gamePhase = roomRepository.getGamePhase(roomCode)

    try:
        await websocket.send_json(roomRepository.generateHandshake())

        while True:
            event = await websocket.recieve_json()
            if gamePhase == "lobby":
                message = roomRepository.handleLobbyWsEvent(event)
                for player in roomRepository.getPlayerList():
                    await player.websocket.send_json(message)

            if gamePhase == "play":
                message = roomRepository.handlePlayWsEvent(event)
                for player in roomRepository.getPlayerList():
                    await player.websocket.send_json(message)

    except WebSocket.exceptions.ConnectionClosedError:
        Exception("Connection closed")


@router.websocket("/join/{roomCode}/{name}")
async def joinAndConnect(websocket: WebSocket, roomCode: str, name: str):
    if not roomRepository.roomExists(roomCode):
        raise HTTPException(status_code=404, detail="Room not found")

    await websocket.accept()

    roomRepository.addPlayer(roomCode, name, websocket)
    gamePhase = roomRepository.getGamePhase(roomCode)

    try:
        await websocket.send_json(roomRepository.generateHandshake())

        while True:
            event = await websocket.recieve_json()
            if gamePhase == "lobby":
                handshake = roomRepository.handleLobbyWsEvent(event)
                await websocket.send_json(handshake)

            if gamePhase == "play":
                handshake = roomRepository.handlePlayWsEvent(event)
                await websocket.send_json(handshake)

    except WebSocket.exceptions.ConnectionClosedError:
        Exception("Connection closed")
