from fastapi import APIRouter, Depends, status
from .. import schemas
from .. import models
from sqlalchemy.orm import Session
from ..database import get_db

router = APIRouter(
    prefix="/writers",
    tags=['Writers']
)

@router.post("/", response_model=schemas.Writer)
def create_user(writer: schemas.WriterCreate, db: Session = Depends(get_db)):
    
    new_writer = models.Writer(**writer.dict())
    db.add(new_writer)
    db.commit()
    db.refresh(new_writer)
    return new_writer

