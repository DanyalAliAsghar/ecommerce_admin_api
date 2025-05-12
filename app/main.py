from fastapi import FastAPI
from .routers import products

app = FastAPI()

app.include_router(products.router, prefix="/products", tags=["products"])


@app.get("/")
def read_root():
    return {"message": "E-commerce Admin API is working"}
