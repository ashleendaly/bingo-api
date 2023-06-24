from fastapi import APIRouter, HTTPException, WebSocket
from src.utils.generateUniqueRoomCode import generateUniqueRoomCode, generateUniqueUserId
from src.repository.instance import roomRepository

router = APIRouter()


@router.post("/create", summary="Create a new room", description="Generates a unique room code that anyone can access")
def createRoom():
    room_code = generateUniqueRoomCode()
    user_id = generateUniqueUserId()
    roomRepository.createRoom(room_code, user_id)
    return {"room_code": room_code, "user_id": user_id}

#TODO: join and websocket should be 1 endpoint
@router.put("/{room_code}", summary="Join a room")
def joinRoom(room_code: str):
    if roomRepository.roomExists(room_code):
        user_id = generateUniqueUserId()
        roomRepository.joinRoom(room_code, user_id)
        return {"user_id": user_id}
    else:
        raise HTTPException(status_code=404, detail="Room not found")


@router.websocket("/ws/{room_code}/{user_id}", summary="Connect to a room")
async def websocketEndpoint(websocket: WebSocket, room_code: str, user_id: str):
    if not roomRepository.roomExists(room_code):        
        raise HTTPException(status_code=404, detail="Room not found")
    
    if not roomRepository.userInRoom(room_code, user_id):
        raise HTTPException(status_code=403, detail="User not in room")
            
    await websocket.accept()

    try:
        roomRepository.addWebSocketToRoom(room_code, websocket)
        while True:
            eventUpdate = await websocket.receive_json()
            eventId = eventUpdate["id"]
            # TODO: increment event count

            for ws in roomRepository.getAllWebSocketsInRoom(room_code):
                await ws.send_json({"id": eventId})

    except WebSocket.exceptions.ConnectionClosedError:
        roomRepository.removeWebSocketFromRoom(room_code, websocket)

