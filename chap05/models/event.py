from typing import List
from pydantic import BaseModel

class Event(BaseModel):
    id: int
    title: str
    image: str
    descriptions: str
    tags: List[str]
    location: str