from typing import List, Optional
from sqlmodel import SQLModel,Field,Column, JSON

# this will create table
# this for validation and DB operation
class Event(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    title: str
    image: str
    description: str
    tags: List[str] = Field(sa_column=Column(JSON))
    location: str
    # user_id: int | None = Field(default=None, foreign_key="user.id")
    class Config:
        pk_with_sequence = True # auto increment


# this will not create table
# this will be used for validation
class EventUpdate(SQLModel):
    title: Optional[str]
    image: Optional[str]
    description: Optional[str]
    tags: Optional[List[str]]
    location: Optional[str]