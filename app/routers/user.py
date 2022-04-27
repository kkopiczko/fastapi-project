from fastapi import APIRouter, Depends, status
from .. import schemas
from .. import models
from sqlalchemy.orm import Session
from ..database import get_db

router = APIRouter(
    prefix="/users",
    tags=['Users']
)