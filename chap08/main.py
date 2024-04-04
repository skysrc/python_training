from fastapi import FastAPI
from fastapi.responses import RedirectResponse
import uvicorn
from database.connection import conn
from routes.events import router as EventRouter
from routes.users import router as UserRouter
from contextlib import asynccontextmanager
from fastapi.middleware.cors import CORSMiddleware

@asynccontextmanager
async def lifespan(app: FastAPI):
    # before application start : 
    conn()
    yield
    # Do nothing
    

app = FastAPI(lifespan=lifespan)
app.include_router(EventRouter, prefix="/event")
app.include_router(UserRouter, prefix="/user")

#register origin - domain that are allowed to access this APi from browser
origins = ['http://localhost:3000','http://127.0.0.1:5500'] # all origins are allowed
app.add_middleware(CORSMiddleware, 
                   allow_origins = origins,
                   allow_credentials = True,
                   allow_methods = ["*"],
                   allow_headers = ["*"])

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