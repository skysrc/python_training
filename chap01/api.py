from fastapi import FastAPI
app = FastAPI() # instantiate a FastAPi program

# API node
@app.get('/')
async def welcome() -> dict:
    return{"message" : "Hello World"}

@app.get('/home')
async def home() -> dict:
    return{"message" : "Welcome Home"}