from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from ..database import get_db
from .. import crud, schemas

router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    user_model = schemas.User(**user.dict())
    return crud.create_user(db, user=user_model)

@router.get("/", response_model=List[schemas.User])
def get_users(db: Session = Depends(get_db)):
    return crud.get_users(db)
