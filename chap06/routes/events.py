from typing import List
from fastapi import APIRouter, HTTPException,status
from fastapi.params import Body
from models.event import Event
from database.connection import getConnection
import json

router = APIRouter()

events=[]

@router.put('/event-update/{id}')
async def update_event(id: int, event: Event = Body())-> dict:
     conn = getConnection()
     cursor = conn.cursor()
     sql = f"SELECT * FROM event WHERE id = {id}"
     cursor.execute(sql)
     row = cursor.fetchone()

     if row:
          # this id / event exists
          sql = f"""UPDATE event SET 
                title = '{event.title}',
                image = '{event.image}',
                description = '{event.description}',
                tags = '{json.dumps(event.tags)}',
                location = '{event.location}'
                WHERE id = {id}
          """
          cursor.execute(sql)
          conn.commit()
          cursor.close()
          conn.close()
          return {"message": "Event successfully updated"}
     else:
          raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Supplied id does not exists")
     

@router.get("/", response_model=List[Event])
async def retrieve_all_event() -> List[Event]:
    conn = getConnection()
    sql = "SELECT * FROM event"
    cursor = conn.cursor()
    cursor.execute(sql)
    rows = cursor.fetchall()
    event_list = []
    for row in rows:
         params = {"id": row[0], "title": row[1], "image": row[2], "description": row[3], "tags": json.loads(row[4]), "location":row[5]}
         event = Event(**params)
        #  event.title = row[1]
        #  event.image = row[2]
        #  event.description = row[3]
        #  event.tags = row[4]
        #  event.location = row[5]
         event_list.append(event)
    cursor.close()
    conn.close()
    return event_list

@router.get("/{id}", response_model=Event)
async def retrieve_event(id: int) -> Event:
    conn = getConnection()
    sql = f"SELECT * FROM event WHERE id = {id}"
    cursor = conn.cursor()
    cursor.execute(sql)
    row = cursor.fetchone()
    if row:
         params={"id": row[0], "title": row[1], "image": row[2], "description": row[3], "tags": json.loads(row[4]), "location":row[5]}
         return Event(**params)
    else:
         raise HTTPException(
            status_code=status. HTTP_404_NOT_FOUND,
            detail="Event with supplied ID does not exist")
    # for event in events:
    #     if event.id == id:
    #         return event
    # raise HTTPException(
    #     status_code=status. HTTP_404_NOT_FOUND,
    #     detail="Event with supplied ID does not exist")


@router.post("/new")
async def create_event(body: Event = Body(...)) -> dict:
        conn = getConnection()
        sql = """
        INSERT INTO event (title,image, description, tags, location)
        VALUES('{}','{}','{}','{}','{}')
        """
        sql = sql.format(body.title,body.image, body.description, json.dumps(body.tags), body.location)
        print(sql)
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()
        cursor.close()
        conn.close()
        return {"message": "Event created successfully"}

@router.delete("/{id}")
async def delete_event(id: int) -> dict:
      conn = getConnection()
      sql = f"""
        DELETE FROM event WHERE id = {id}
        """
      cursor = conn.cursor()
      ok = cursor.execute(sql)
      conn.commit()
      count = cursor.rowcount
      cursor.close()
      conn.close()
      if count > 0 :

           return {"message": "Event successfully deleted"}
      else:
           raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail="Event with supplied ID does not exists")

    #   for event in events:
    #         if event.id == id:
    #               events.remove(event)
    #               return {"message": "Event deleted successfully"}
    #         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
    #                             detail="Event with supplied ID does not exists")
      

@router.delete("/")
async def delete_all_events() -> dict:
    conn = getConnection()
    sql = """DELETE FROM event"""
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()
    count = cursor.rowcount
    cursor.close()
    conn.close()
    if count > 0 :

        return {"message": f"{count} Event successfully deleted"}
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="No record deleted")

