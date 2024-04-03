from fastapi import APIRouter, Form, Request, HTTPException, status
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates

router = APIRouter()

todo_list = [
    {"id": 1, "title": "todo 1"},
    {"id": 2, "title": "todo 2"}
]
templates = Jinja2Templates(directory="templates/")

@router.post('/todo')
async def add_todo(request: Request, title: str = Form(...)):
    index = len(todo_list)
    todo_list.append({"id": index, "title": title})
    return templates.TemplateResponse("todo.html", {
        "request": request,
        "todos": todo_list,
        "name": "John Doe"
    })

@router.get("/todo")
def show(request: Request):
    return templates.TemplateResponse("todo.html",{
                                          "request": request,
                                          "todos": todo_list
                                      })

@router.get("/todo-form")
async def show_form(request: Request):
    return templates.TemplateResponse("todo_form.html", {
        "request": request
    })

@router.get("/todo/{index}")
async def todo_delete(index: int, request: Request):
  todo_list.pop(index)
  return RedirectResponse("/todo")