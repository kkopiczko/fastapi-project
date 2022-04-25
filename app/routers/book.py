from fastapi import APIRouter, status
from ..schemas import BookCreate
from sqlalchemy.orm import Session

router = APIRouter(
    prefix="/books",
    tags=['Books']
)

@router.post("/")
def add_book(book: BookCreate):
    return {"new_post": book.dict()}