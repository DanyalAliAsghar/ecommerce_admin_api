# tests/test_products.py

from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_product():
    response = client.post("/products/", json={"name": "Product A", "category": "Category 1", "brand": "Brand X", "price": 100.0, "description": "A great product"})
    assert response.status_code == 200
    assert response.json()["name"] == "Product A"

def test_get_product():
    response = client.get("/products/1")
    assert response.status_code == 200
    assert response.json()["id"] == 1
