from cgitb import text
from lib2to3.pytree import Base
from pydantic import BaseModel

class BookCreate(BaseModel):
    title: str
    author: str
    yearPublished: int
    description: str