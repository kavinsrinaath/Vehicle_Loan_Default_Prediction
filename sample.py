from fastapi import FastAPI
from pydantic import BaseModel


class User(BaseModel):
    email: str
    password: str


app = FastAPI()


@app.post("/login")
def login(user: User):
    # ...
    # do some magic
    # ...
    return {"msg": "login successful"}