from typing import List
from fastapi import APIRouter, Depends, HTTPException,status
from fastapi.params import Body
from models.event import Event, EventUpdate
from database.connection import get_session
from sqlmodel import select, delete
from auth.authenticate import authenticate

router = APIRouter()

events=[]

@router.put('/event-update/{id}')
async def update_event(id: int, new_data: EventUpdate = Body(), session=Depends(get_session))-> Event:
     event = session.get(Event, id)
     if event:
          event_data = new_data.model_dump(exclude_unset=True) # unset data to remove
          for key, value in event_data.items(): #item() return list of key in dict
               setattr(event, key, value)
          session.add(event) # add() - for insert and update.
          session.commit()
          session.refresh(event)
          return event
     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                         detail="Supplied id does not exists.")
     

@router.get("/", response_model=List[Event])
async def retrieve_all_event(session=Depends(get_session), user: str =Depends(authenticate)) -> List[Event]:
    statement = select(Event)
    events = session.exec(statement).all()
    return events

@router.get('/{id}', response_model=Event)
async def retrieve_event(id: int, session=Depends(get_session))-> Event:
     event = session.get(Event,id)
     if event:
          return event
     raise HTTPException(
            status_code=status. HTTP_404_NOT_FOUND,
            detail="Event with supplied ID does not exist")

# Depends() - will run first before anything else
@router.post("/new")
async def create_event(new_event: Event, session=Depends(get_session)) -> dict:
       session.add(new_event)
       session.commit()
       session.refresh(new_event) # repopulate the obj
       return {"message": "Event created successfully"}

@router.delete("/{id}")
async def delete_event(id: int, session=Depends(get_session)) -> dict:
     event = session.get(Event, id)
     if event:
          session.delete(event)
          session.commit()
          return {
          "message": "Event deleted successfully"
          }
     
     raise HTTPException(
          status_code=status.HTTP_404_NOT_FOUND,
          detail="Event with supplied ID does not exist"
          )


@router.delete("/")
async def delete_all_events(session=Depends(get_session)) -> dict:
     statement = delete(Event).where(1==1)
     session.exec(statement)
     session.commit()

     #another approach
     # session.query(Event).delete()
     # session()

     return {"message": "All events deleted successfully"}