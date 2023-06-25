from fastapi import FastAPI
from src.routes import room
from src.repository.instance import roomRepository, incidentRepository

app = FastAPI(title="Bingo API", docs_url="/")
app.include_router(room.router, prefix="/room", tags=["room"])
app.state.roomRepository = roomRepository
app.state.incidentRepository = incidentRepository
