from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

# User Schema
class UserBase(BaseModel):
    name: str
    email: str

class UserCreate(UserBase):
    pass

class User(UserBase):
    id: int

    class Config:
        orm_mode = True

# Product Schema
class ProductBase(BaseModel):
    name: str
    price: float

class ProductCreate(ProductBase):
    pass

class Product(ProductBase):
    id: int

    class Config:
        orm_mode = True

# Order Schema
class OrderBase(BaseModel):
    user_id: int
    date: datetime

class OrderCreate(BaseModel):
    user_id: int
    product_ids: List[int]

class Order(OrderBase):
    id: int
    products: List[Product]

    class Config:
        orm_mode = True
