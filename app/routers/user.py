from fastapi import APIRouter, Depends, status, HTTPException
from .. import schemas, models, utils
from sqlalchemy.orm import Session
from ..database import get_db
from datetime import datetime

router = APIRouter(
    prefix="/users",
    tags=['Users']
)

@router.post("/")
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    hashed_password = utils.hash(user.password)
    user_with_hashed_password = {"email": user.email, "hashed_password": hashed_password, "created_at": datetime.now()}
    # user.hashed_password = hashed_password

    new_user = models.User(**user_with_hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@router.get("/")
def get_users(db: Session = Depends(get_db)):
    users = db.query(models.User).all()
    return users

@router.get("/{id}")
def get_user_by_id(id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'User with an id {id} does not exist')
    return user