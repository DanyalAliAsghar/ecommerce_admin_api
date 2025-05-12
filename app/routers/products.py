# app/routers/products.py

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import crud, schemas
from app.database import get_db

router = APIRouter()

# Create a new product
@router.post("/", response_model=schemas.ProductOut)
def create_product(product: schemas.ProductCreate, db: Session = Depends(get_db)):
    return crud.create_product(db, product)

# Get all products
@router.get("/", response_model=list[schemas.ProductOut])
def get_products(db: Session = Depends(get_db)):
    return crud.get_products(db)

# Get a product by ID
@router.get("/{product_id}", response_model=schemas.ProductOut)
def get_product(product_id: int, db: Session = Depends(get_db)):
    return crud.get_product(db, product_id)

# Get sales data by product ID
@router.get("/{product_id}/sales", response_model=list[schemas.SaleOut])
def get_sales_by_product(product_id: int, db: Session = Depends(get_db)):
    return crud.get_sales_by_product(db, product_id)

# Get inventory by product ID
@router.get("/{product_id}/inventory", response_model=schemas.InventoryOut)
def get_inventory(product_id: int, db: Session = Depends(get_db)):
    return crud.get_inventory(db, product_id)

# Update inventory stock level
@router.put("/{product_id}/inventory", response_model=schemas.InventoryOut)
def update_inventory(product_id: int, stock_level: int, db: Session = Depends(get_db)):
    return crud.update_inventory(db, product_id, stock_level)
