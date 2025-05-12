# app/crud.py

from sqlalchemy.orm import Session
from . import models, schemas

# Create a product
def create_product(db: Session, product: schemas.ProductCreate):
    db_product = models.Product(**product.dict())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

# Get all products
def get_products(db: Session):
    return db.query(models.Product).all()

# Get a product by ID
def get_product(db: Session, product_id: int):
    return db.query(models.Product).filter(models.Product.id == product_id).first()

# Create a sale
def create_sale(db: Session, sale: schemas.SaleCreate):
    db_sale = models.Sale(**sale.dict())
    db.add(db_sale)
    db.commit()
    db.refresh(db_sale)
    return db_sale

# Get sales data by product
def get_sales_by_product(db: Session, product_id: int):
    return db.query(models.Sale).filter(models.Sale.product_id == product_id).all()

# Get inventory status for a product
def get_inventory(db: Session, product_id: int):
    return db.query(models.Inventory).filter(models.Inventory.product_id == product_id).first()

# Update inventory stock level
def update_inventory(db: Session, product_id: int, stock_level: int):
    inventory = db.query(models.Inventory).filter(models.Inventory.product_id == product_id).first()
    if inventory:
        inventory.stock_level = stock_level
        db.commit()
        db.refresh(inventory)
        return inventory
    return None
