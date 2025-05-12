from app import models
from app.database import SessionLocal
from datetime import datetime, timedelta
import random

def populate_demo_data():
    db = SessionLocal()

    # Create products
    products = [
        models.Product(name="Wireless Mouse", category="Electronics", brand="LogiTech", price=29.99, description="Ergonomic wireless mouse"),
        models.Product(name="Bluetooth Headphones", category="Electronics", brand="Sony", price=79.99, description="Noise cancelling headphones"),
        models.Product(name="Running Shoes", category="Footwear", brand="Nike", price=120.00, description="Lightweight running shoes"),
        models.Product(name="T-shirt", category="Apparel", brand="H&M", price=15.00, description="100% cotton T-shirt"),
        models.Product(name="Smart Watch", category="Wearables", brand="Apple", price=299.99, description="Series 7 Smartwatch"),
        models.Product(name="Gaming Keyboard", category="Electronics", brand="Razer", price=99.99, description="Mechanical keyboard with RGB lighting"),
        models.Product(name="Office Chair", category="Furniture", brand="Ikea", price=149.99, description="Comfortable ergonomic chair"),
        models.Product(name="Backpack", category="Accessories", brand="North Face", price=89.99, description="Durable hiking backpack"),
        models.Product(name="Water Bottle", category="Home & Kitchen", brand="Hydro Flask", price=39.99, description="Insulated stainless steel bottle"),
        models.Product(name="Electric Toothbrush", category="Personal Care", brand="Oral-B", price=59.99, description="Rechargeable electric toothbrush"),
    ]
    db.add_all(products)
    db.commit()

    # Add inventory
    for product in db.query(models.Product).all():
        inventory = models.Inventory(
            product_id=product.id,
            stock_level=random.randint(10, 100)
        )
        db.add(inventory)
    db.commit()

    # Add sales data
    platforms = ["Amazon", "Walmart"]
    for product in db.query(models.Product).all():
        for i in range(5):  # 5 sales entries per product
            sale = models.Sale(
                product_id=product.id,
                quantity_sold=random.randint(1, 5),
                sale_date=datetime.utcnow() - timedelta(days=random.randint(0, 30)),
                platform=random.choice(platforms),
                unit_price=product.price
            )
            db.add(sale)
    db.commit()

    db.close()

if __name__ == "__main__":
    populate_demo_data()
