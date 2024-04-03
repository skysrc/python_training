from fastapi import FastAPI
from routes.events import router as EventRouter
from routes.users import router as UserRouter

app = FastAPI()
app.include_router(EventRouter)
app.include_router(UserRouter)


