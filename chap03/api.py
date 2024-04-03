from fastapi import FastAPI
from todo import router

app = FastAPI()
app.include_router(router)

