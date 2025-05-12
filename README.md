# E-Commerce Admin API

This is a FastAPI-based backend API for an e-commerce admin dashboard. It provides endpoints to manage products, sales, and inventory, and allows for revenue analysis over different periods. It supports operations such as creating products, retrieving sales data, updating inventory, and generating insights.

## Features

1. **Sales Status**:
   - Retrieve, filter, and analyze sales data.
   - Analyze revenue on a daily, weekly, monthly, and annual basis.
   - Compare revenue across different periods and categories.
   - View sales data by date range, product, and category.

2. **Inventory Management**:
   - View current inventory status, including low stock alerts.
   - Update inventory levels and track changes over time.

## Technologies Used

- Python 3.8+
- FastAPI
- SQLAlchemy (ORM)
- Pydantic (data validation)

## Setup

### Prerequisites

- Python 3.8 or higher
- Virtual environment (recommended)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/DanyalAliAsghar/ecommerce_admin_api.git
   cd ecommerce-admin-api

## Populate Demo Data

To populate the database with demo data, run the following command:

```bash
python -m app.scripts.demo_data