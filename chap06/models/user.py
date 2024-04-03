from typing import List, Optional
from pydantic import BaseModel, EmailStr
from models.event import Event

class User(BaseModel):
    email: EmailStr
    title: str
    password: str
    events: Optional[List[Event]]

class UserSignIn(BaseModel):
    email: EmailStr
    password: str

class NewUser(User):
    pass