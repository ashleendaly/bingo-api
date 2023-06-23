from typing import List
from fastapi import APIRouter, Request

from src.models.bingo import EventList

router = APIRouter()


@router.post("/eventlist",
             summary="Create a new event list")
def addEventList(eventList: EventList, request: Request):
    request.app.state.bingo_repository.addEventList(eventList)
    return {"id": eventList.id}


@router.get("/eventlist/{id}",
            summary="Get an event list by id",
            response_model=EventList)
def getEventList(id: str, request: Request):
    eventList = request.app.state.bingo_repository.getEventList(id)
    return eventList
