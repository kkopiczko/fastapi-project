# from typing import List, Optional
from pydantic import BaseModel

class BookBase(BaseModel):
    title: str
    year_published: int
    description: str | None = None

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
    books_written: list[Book] = []

    class Config:
        orm_mode = True

class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int

    class Config:
        orm_mode = True