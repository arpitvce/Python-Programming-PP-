from fastapi import FastAPI
from pydantic import BaseModel

app=FastAPI()

class Numbers(BaseModel):
    a:int
    b:int

@app.post("/add")
def add(number:Numbers):
    return {"sum=":number.a+number.b}


