from fastapi import APIRouter

router = APIRouter()

todo_list = []

@router.get("/todo")
async def todo_home() -> dict:
    #FastAPI auto convert dict to JSON
    return {"message": "todo home!"}

@router.post("/todo")
async def add_todo(todo: dict) -> dict:
 todo_list.append(todo)
 return {"message": todo_list}


