from fastapi import FastAPI
from models import Products

app=FastAPI()

def greet_logic():
    return {"message":"Welcome"}
product=[
          Products(id=1,name="Noodles",description="Spicy",price=290,quantity=2),
          Products(id=2,name="Pasta",description="Saucy",price=300,quantity=4),
          Products(id=3,name="Pizza",description="Cheesy",price=440,quantity=6),
          Products(id=4,name="Chaat",description="Tasty",price=220,quantity=5)
          ]

@app.get('/')
def greet():
    return greet_logic()

@app.get('/products')
def products():
    return product
