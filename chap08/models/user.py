from typing import List, Optional
from pydantic import BaseModel, EmailStr
from models.event import Event
from sqlmodel import Relationship, SQLModel,Field,Column, JSON,String

class User(SQLModel, table=True):
    email: str = Field(String, primary_key=True)
    title: str
    password: str
    # https://sqlmodel.tiangolo.com/tutorial/relationship-attributes/define-relationships-attributes/
    # events: list["Event"] = Relationship(back_populates="Event")
    # events: Optional[List[Event]]


class UserSignIn(BaseModel):
    email: EmailStr
    password: str

class NewUser(User):
    pass