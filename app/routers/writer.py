from fastapi import APIRouter, Depends, status, HTTPException
from .. import schemas
from .. import models
from sqlalchemy.orm import Session
from ..database import get_db

router = APIRouter(
    prefix="/writers",
    tags=['Writers']
)

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.Writer)
def create_writer(writer: schemas.WriterCreate, db: Session = Depends(get_db)):
    
    new_writer = models.Writer(**writer.dict())
    db.add(new_writer)
    db.commit()
    db.refresh(new_writer)
    return new_writer

@router.get("/", response_model=list[schemas.Writer])
def get_writers(db: Session = Depends(get_db)):
    writers = db.query(models.Writer).all()
    return writers

@router.get("/{id}", response_model=schemas.Writer)
def get_writer_by_id(id: int, db: Session = Depends(get_db)):
    writer = db.query(models.Writer).filter(models.Writer.id == id).first()
    if not writer:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Writer with an id {id} does not exist')
    return writer