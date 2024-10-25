from sqlalchemy import Column, Integer, String, Float, ForeignKey, Table
from sqlalchemy.orm import relationship
from .database import Base

user_product_table = Table('user_product', Base.metadata,
                           Column('user_id', Integer, ForeignKey('users.id')),
                           Column('product_id', Integer, ForeignKey('products.id'))
                           )

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)

    orders = relationship("Order", back_populates="user")
    products = relationship("Product", secondary=user_product_table, back_populates="users")

class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    price = Column(Float)

    users = relationship("User", secondary=user_product_table, back_populates="products")

class Order(Base):
    __tablename__ = 'orders'

    id = Column(Integer, primary_key=True, index=True)
    date = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))

    user = relationship("User", back_populates="orders")
    products = relationship("Product")
