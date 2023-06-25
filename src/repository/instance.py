import os
import dotenv
from src.repository.incidentRepository import InMemoryIncidentRepository
from src.repository.roomRepository import InMemoryRoomRepository

dotenv.load_dotenv()

if os.getenv("DATABSE_URL"):
    # sets_database
    pass
else:
    roomRepository = InMemoryRoomRepository()
    incidentRepository = InMemoryIncidentRepository()
