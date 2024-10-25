from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from ..database import get_db
from .. import crud, schemas

router = APIRouter(prefix="/orders", tags=["Orders"])

@router.post("/", response_model=schemas.Order)
def create_order(order: schemas.OrderCreate, db: Session = Depends(get_db)):
    try:
        new_order = crud.create_order(db, user_id=order.user_id, product_ids=order.product_ids)
        return new_order
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/", response_model=List[schemas.Order])
def get_orders(db: Session = Depends(get_db)):
    return crud.get_orders(db)

@router.get("/user/{user_id}", response_model=List[schemas.Order])
def get_user_orders(user_id: int, db: Session = Depends(get_db)):
    user_orders = crud.get_user_orders(db, user_id=user_id)
    if not user_orders:
        raise HTTPException(status_code=404, detail="No orders found for the given user ID")
    return user_orders

@router.get("/user/{user_id}/products", response_model=List[schemas.Product])
def get_user_ordered_products(user_id: int, db: Session = Depends(get_db)):
    products = crud.get_user_ordered_products(db, user_id=user_id)
    if not products:
        raise HTTPException(status_code=404, detail="No products found for the given user ID")
    return products
