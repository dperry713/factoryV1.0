# Factory Management System

A robust Flask-based system for managing factory operations including employees, products, orders, customers, and production records.

## Features

- Employee Management
  - Track employee details and positions
  - Analyze employee performance metrics

- Product Management
  - Maintain product catalog with pricing
  - Track top-selling products
  - Paginated product listing

- Order Management
  - Process customer orders
  - Track order quantities
  - Paginated order listing

- Customer Management
  - Maintain customer database
  - Calculate customer lifetime value
  - Track customer orders

- Production Management
  - Record production activities
  - Evaluate production efficiency
  - Track production dates and quantities

## Technical Stack

- Flask web framework
- SQLAlchemy ORM
- SQLite database
- Flask-Migrate for database migrations


## API Endpoints

### Employees
- GET /employees/ - List all employees
- GET /employees/<id> - Get employee details
- POST /employees/ - Create new employee
- PUT /employees/<id> - Update employee
- DELETE /employees/<id> - Delete employee
- GET /employees/performance - Get employee performance metrics

### Products
- GET /products/ - List all products (paginated)
- GET /products/<id> - Get product details
- POST /products/ - Create new product
- PUT /products/<id> - Update product
- DELETE /products/<id> - Delete product
- GET /products/top-selling - Get top selling products

### Orders
- GET /orders/ - List all orders (paginated)
- GET /orders/<id> - Get order details
- POST /orders/ - Create new order
- PUT /orders/<id> - Update order
- DELETE /orders/<id> - Delete order

### Customers
- GET /customers/ - List all customers
- GET /customers/<id> - Get customer details
- POST /customers/ - Create new customer
- PUT /customers/<id> - Update customer
- DELETE /customers/<id> - Delete customer
- GET /customers/lifetime-value - Get customer lifetime value analysis

### Production
- GET /production/ - List all production records
- GET /production/<id> - Get production record details
- POST /production/ - Create new production record
- PUT /production/<id> - Update production record
- DELETE /production/<id> - Delete production record
- GET /production/efficiency - Get production efficiency metrics

## Setup and Installation

1. Clone the repository
2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
pip install flask flask-sqlalchemy flask-migrate
flask db init
flask db migrate
flask db upgrade
python run.py
