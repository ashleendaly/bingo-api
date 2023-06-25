import random
import string
import uuid


def generateUniqueUserId():
    return str(uuid.uuid4())


def generateUniqueRoomCode():
    code = ''.join(random.choices(string.digits, k=6))
    return code
    # TODO: Check if code is unique
