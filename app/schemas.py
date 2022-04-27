from typing import Optional, List
from pydantic import BaseModel, EmailStr
from datetime import datetime

class BookBase(BaseModel):
    title: str
    year_published: int
    description: Optional[str] = None

class BookCreate(BookBase):
    pass

class Book(BookBase):
    id: int
    author_id: int

    # setting a config value to tell Pydanticto read the data even if it is not a dict, but an ORM model
    class Config:
        orm_mode = True

class WriterBase(BaseModel):
    name: str
    last_name: str

class WriterCreate(WriterBase):
    pass

class Writer(WriterBase):
    id: int
    books_written: List[Book] = []

    class Config:
        orm_mode = True

class UserBase(BaseModel):
    email: EmailStr


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True