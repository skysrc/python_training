from typing import List
from fastapi import APIRouter, HTTPException,status
from fastapi.params import Body
from models.event import Event

router = APIRouter()

events=[]

@router.get("/", response_model=List[Event])
async def retrieve_all_event() -> List[Event]:
    return events

@router.get("/{id}", response_model=Event)
async def retrieve_event(id: int) -> Event:
    for event in events:
        if event.id == id:
            return event
    raise HTTPException(
        status_code=status. HTTP_404_NOT_FOUND,
        detail="Event with supplied ID does not exist")


@router.post("/new")
async def create_event(body: Event = Body(...)) -> dict:
        events.append(body)
        return {"message": "Event created successfully"}

@router.delete("/{id}")
async def delete_event(id: int) -> dict:
      for event in events:
            if event.id == id:
                  events.remove(event)
                  return {"message": "Event deleted successfully"}
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail="Event with supplied ID does not exists")
      

@router.delete("/")
async def delete_all_events() -> dict:
    events.clear()
    return {"message": "Events deleted successfully"}
