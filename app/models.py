from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from .database import Base

class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    category = Column(String)
    brand = Column(String)
    price = Column(Float)
    description = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)

    sales = relationship("Sale", back_populates="product")
    inventory = relationship("Inventory", back_populates="product", uselist=False)

class Inventory(Base):
    __tablename__ = "inventory"
    id = Column(Integer, primary_key=True)
    product_id = Column(Integer, ForeignKey("products.id"))
    stock_level = Column(Integer)
    last_updated = Column(DateTime, default=datetime.utcnow)

    product = relationship("Product", back_populates="inventory")

class Sale(Base):
    __tablename__ = "sales"
    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey("products.id"))
    quantity_sold = Column(Integer)
    sale_date = Column(DateTime, default=datetime.utcnow)
    platform = Column(String)  # Amazon or Walmart
    unit_price = Column(Float)

    product = relationship("Product", back_populates="sales")
