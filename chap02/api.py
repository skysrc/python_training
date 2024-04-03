from fastapi import FastAPI
from todo import router
from book import router as bookRouter

app = FastAPI()
app.include_router(router)
app.include_router(bookRouter)

