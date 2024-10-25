from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from . import models
from datetime import datetime

# User CRUD operations
def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

def create_user(db: Session, user: models.User):
    try:
        db.add(user)
        db.commit()
        db.refresh(user)
        return user
    except IntegrityError:
        db.rollback()
        raise ValueError("User with the same email already exists")

def get_users(db: Session):
    return db.query(models.User).all()

# Product CRUD operations
def get_products(db: Session):
    return db.query(models.Product).all()

def create_product(db: Session, product: models.Product):
    db.add(product)
    db.commit()
    db.refresh(product)
    return product

# Order CRUD operations
def create_order(db: Session, user_id: int, product_ids: list[int]):
    # Validate user existence
    user = get_user(db, user_id)
    if not user:
        raise ValueError(f"User with ID {user_id} does not exist")
    
    # Validate product existence
    products = db.query(models.Product).filter(models.Product.id.in_(product_ids)).all()
    if len(products) != len(product_ids):
        raise ValueError("One or more product IDs are invalid")
    
    # Create order
    new_order = models.Order(date=datetime.now().strftime("%Y-%m-%d %H:%M:%S"), user_id=user_id)
    new_order.products = products
    db.add(new_order)
    db.commit()
    db.refresh(new_order)
    return new_order

def get_orders(db: Session):
    return db.query(models.Order).all()

def get_user_orders(db: Session, user_id: int):
    return db.query(models.Order).filter(models.Order.user_id == user_id).all()

def get_user_ordered_products(db: Session, user_id: int):
    # Get all products ordered by a specific user
    user_orders = get_user_orders(db, user_id)
    product_list = []
    for order in user_orders:
        product_list.extend(order.products)
    return product_list