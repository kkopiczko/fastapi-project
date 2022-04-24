from fastapi import FastAPI
from .routers import book

app = FastAPI()

# create an endpoint

@app.get("/")
def root():
    return {"data": "root"}

app.include_router(book.router)

