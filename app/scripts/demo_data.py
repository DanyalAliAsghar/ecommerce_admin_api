# app/scripts/demo_data.py

from app import models
from app.database import SessionLocal
from datetime import datetime

def populate_demo_data():
    db = SessionLocal()

    # Create products
    product1 = models.Product(name="Product A", category="Category 1", brand="Brand X", price=100.0, description="A great product")
    product2 = models.Product(name="Product B", category="Category 2", brand="Brand Y", price=150.0, description="Another great product")
    db.add_all([product1, product2])
    db.commit()

    # Add inventory
    inventory1 = models.Inventory(product_id=1, stock_level=50)
    inventory2 = models.Inventory(product_id=2, stock_level=30)
    db.add_all([inventory1, inventory2])
    db.commit()

    # Add sales
    sale1 = models.Sale(product_id=1, quantity_sold=10, sale_date=datetime.utcnow(), platform="Amazon", unit_price=100.0)
    sale2 = models.Sale(product_id=2, quantity_sold=5, sale_date=datetime.utcnow(), platform="Walmart", unit_price=150.0)
    db.add_all([sale1, sale2])
    db.commit()

if __name__ == "__main__":
    populate_demo_data()
