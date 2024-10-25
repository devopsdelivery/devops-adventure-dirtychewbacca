from fastapi import FastAPI
from .routers import users, products, orders
from .database import engine
from . import models

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

app.include_router(users.router)
app.include_router(products.router)
app.include_router(orders.router)
