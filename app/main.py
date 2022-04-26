from fastapi import FastAPI
from .routers import book
from . import models
from .database import engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()




# create an endpoint

@app.get("/")
def root():
    return {"data": "root"}

app.include_router(book.router)

