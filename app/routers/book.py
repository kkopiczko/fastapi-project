from fastapi import APIRouter
from ..schemas import BookCreate

router = APIRouter(
    prefix="/books",
    tags=['Books']
)

@router.post("/")
def add_book(book: BookCreate):
    return {"new_post": book.dict()}