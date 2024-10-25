from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from ..database import get_db
from .. import crud, schemas

router = APIRouter(prefix="/products", tags=["Products"])

@router.post("/", response_model=schemas.Product)
def create_product(product: schemas.ProductCreate, db: Session = Depends(get_db)):
    product_model = schemas.Product(**product.dict())
    return crud.create_product(db, product=product_model)

@router.get("/", response_model=List[schemas.Product])
def get_products(db: Session = Depends(get_db)):
    return crud.get_products(db)
