from fastapi import APIRouter, HTTPException, Path, status
from model import TodoItem, TodoItems

router = APIRouter()

todo_list = []

@router.get("/todo", response_model=TodoItems)
async def todo_home() -> dict:
    #FastAPI auto convert dict to JSON
    return {"todos": todo_list}

@router.post("/todo", status_code=201)
async def add_todo(todo: TodoItem) -> dict:
 todo_list.append(todo)
 return {"message": todo_list}

# UPDATE a book 
@router.put("/todo/{id}")
async def book_update(todo: TodoItem, id: int = Path(..., title="Todo item id", gt=0, lt=100))-> dict:
   for index in range(len(todo_list)):
    targetTodo = todo_list[index]
    if targetTodo.id == id:
        targetTodo.item = todo.item
        return {"todos": todo_list}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="ID does not exists")


@router.get("/todo/{id}")
async def get_single_todo(id: int = Path(..., title="the id of the todo to retrieve"))-> dict :
   for todo in todo_list:
      if todo.id == id:
          return {"todo": todo}
      #id not found
      raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Todo with supplied ID doesn't exists")


@router.delete("/todo/{id}")
async def todo_delete(id: int) -> dict:
   for index in range(len(todo_list)):
    todo = todo_list[index]
    if todo.id == id:
       todo_list.pop(index)
       return {"message": "todo deleted successfully"}
   
   raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="ID does not exists")
    
   
