from fastapi import APIRouter, Path, Query
from pydantic import BaseModel
router = APIRouter()

# this class is used to validate data
class Book(BaseModel):
   id: int
   name: str
   publisher: str
   isbn: str

books = []

@router.post("/book")
async def book_validate(book: Book) -> dict:
 books.append(book)
 return {"books": books}

# RETRIEVE a node to return all books
@router.get("/book")
async def book_all() -> dict:
    return {"books": books}

# UPDATE a book 
@router.put("/book/{id}")
async def book_update(book: Book, id: int = Path(..., title="book id", gt=0, lt=100))-> dict:
   for book2 in books:
      if book2.id == id:
            book2.name = book.name

   return {"books": books}

@router.delete("/book/{id}")
async def book_delete(id: int) -> dict:
   index = 0
   for book in books:
        if book.id == id:
            books.pop(index)
        index +=1
        return {"books": books}
   

# Retrieve a single record with query parameter
@router.get("/single-book")
def book_single(id: int= Query(None), name: str = Query(None)) -> dict:
    print(f"id = {id}")
    for book in books:
        if book.id == id:
            return {"message" : book}
    return {"message": "Book is not found"}