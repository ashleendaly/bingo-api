from fastapi import APIRouter, HTTPException, WebSocket
from src.utils.generateUniqueRoomCode import generateUniqueRoomCode, generateUniqueUserId
from src.repository.instance import roomRepository

router = APIRouter()


@router.post("/", summary="Create a new room")
def createRoom():
    room_code = generateUniqueRoomCode()
    user_id = generateUniqueUserId()
    roomRepository.createRoom(room_code, user_id)
    return {"room_code": room_code, "user_id": user_id}


@router.put("/{room_code}", summary="Join a room")
def joinRoom(room_code: str):
    if roomRepository.roomExists(room_code):
        user_id = generateUniqueUserId()
        roomRepository.joinRoom(room_code, user_id)
        return {"user_id": user_id}
    else:
        raise HTTPException(status_code=404, detail="Room not found")


@router.websocket("/ws/{room_code}/{user_id}")
async def websocketEndpoint(websocket: WebSocket, room_code: str, user_id: str):
    if roomRepository.roomExists(room_code):
        if roomRepository.userInRoom(room_code, user_id):
            await websocket.accept()

            try:
                roomRepository.addWebSocketToRoom(room_code, websocket)
                while True:
                    eventUpdate = await websocket.receive_json()
                    eventId = eventUpdate["id"]
                    eventHasHappened = eventUpdate["hasHappened"]

                    for ws in roomRepository.getAllWebSocketsInRoom(room_code):
                        await ws.send_json({"id": eventId, "hasHappened": eventHasHappened})

            except WebSocket.exceptions.ConnectionClosedError:
                roomRepository.removeWebSocketFromRoom(room_code, websocket)

        else:
            await websocket.close()
            raise HTTPException(status_code=403, detail="User not in room")
    else:
        await websocket.close()
        raise HTTPException(status_code=404, detail="Room not found")
