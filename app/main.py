from fastapi import FastAPI
from .schemas import BookCreate

app = FastAPI()

# create an endpoint

@app.get("/")
def root():
    return {"data": "root"}

@app.post("/books")
def add_book(book: BookCreate):
    return {"new_post": book.dict()}