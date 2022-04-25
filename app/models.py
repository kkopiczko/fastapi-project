from .database import Base

from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)

class Writer(Base):
    __tablename__ = "writers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    last_name = Column(String, index=True)

    books_written = relationship("Book", back_populates="author")

class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    year_published = Column(Integer)
    description = Column(String, index=True)
    author_id = Column(Integer, ForeignKey("writers.id"))

    author = relationship("Writer", back_populates="books_written")

# class Rating(Base):
#     __tablename__ = "ratings"

#     id = Column(Integer, primary_key=True, index=True)
#     email = Column(String, unique=True, index=True)
#     hashed_password = Column(String)
#     is_active = Column(Boolean, default=True)

#     items = relationship("Item", back_populates="owner")