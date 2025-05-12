# app/schemas.py

from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class ProductBase(BaseModel):
    name: str
    category: str
    brand: str
    price: float
    description: Optional[str] = None

class ProductCreate(ProductBase):
    pass

class ProductOut(ProductBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True

class SaleBase(BaseModel):
    quantity_sold: int
    sale_date: datetime
    platform: str
    unit_price: float

class SaleCreate(SaleBase):
    product_id: int

class SaleOut(SaleBase):
    id: int

    class Config:
        orm_mode = True

class InventoryBase(BaseModel):
    stock_level: int
    last_updated: datetime

class InventoryOut(InventoryBase):
    id: int
    product_id: int

    class Config:
        orm_mode = True
