from fastapi import FastAPI
from .routers import book, user, writer, rating
from . import models
from .database import engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()




# create an endpoint

@app.get("/")
def root():
    return {"data": "root"}

app.include_router(book.router)
app.include_router(user.router)
app.include_router(writer.router)
app.include_router(rating.router)

