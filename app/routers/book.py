from fastapi import APIRouter, Depends, status
from .. import schemas
from .. import models
from sqlalchemy.orm import Session
from ..database import get_db
from ..oauth2 import get_current_user


router = APIRouter(
    prefix="/books",
    tags=['Books']
)

@router.post("/", status_code=status.HTTP_201_CREATED)
def add_book(book: schemas.BookCreate, db: Session = Depends(get_db)):
    new_book = models.Book(**book.dict())
    db.add(new_book)
    db.commit()
    db.refresh(new_book)
    return {"new_book": new_book}

@router.get("/")
def get_books(db: Session = Depends(get_db), current_user: int = Depends(get_current_user)):
    print(current_user.id)
    books = db.query(models.Book).all()
    # print(books)
    return {"books": books}

@router.get("/{book_id}")
def get_book_by_id(book_id: int):
    pass