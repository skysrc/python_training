from typing import List
from pydantic import BaseModel

class TodoItem(BaseModel):
 id: int
 item: str
 #give more info in documentation with sample data
 class Config:
    json_schema_extra = {
        "example": {
        "id": 10,
        "item": "Read the next chapter of the book"
        }
    }

class TodoItems(BaseModel):
 todos: List[TodoItem]
 class Config:
    json_schema_extra = {
        "example": {
            "todos": [
                        {
                            "item": "Example schema 1!", "id": 10
                        },
                        {
                            "item": "Example schema 2!", "id": 11
                        }
                    ]
        }
    }