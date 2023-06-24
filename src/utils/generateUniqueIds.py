import random
import string
import uuid

from src.repository.instance import roomRepository


def generateUniqueRoomCode():
    code = ''.join(random.choices(string.digits, k=6))

    if roomRepository.roomExists(code):
        return generateUniqueRoomCode()
    else:
        return code


def generateUniqueUserId():
    return str(uuid.uuid4())
