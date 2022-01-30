from fastapi import FastAPI

app = FastAPI()

# create an endpoint

@app.get("/")
def root():
    return {"data": "root"}