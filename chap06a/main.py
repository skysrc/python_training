from fastapi import FastAPI
from fastapi.responses import RedirectResponse
import uvicorn
from database.connection import conn
from routes.events import router as EventRouter
from routes.users import router as UserRouter
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    # ORM 
    conn()
    yield
    # Do nothing
    

app = FastAPI(lifespan=lifespan)
app.include_router(EventRouter, prefix="/event")
app.include_router(UserRouter, prefix="/user")

# # run this automaticallly when startup the server.
# @app.on_event("startup")
# def on_startup():
#     conn()

# landing node
@app.get("/")
async def home():
    return RedirectResponse(url="/event/")

if __name__ == '__main__':
    uvicorn.run("main:app", host="0.0.0.0", port=8001, reload=False)