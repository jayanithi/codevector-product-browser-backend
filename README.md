# Product Browser Backend

## Tech Stack
- Django
- Django REST Framework
- MySQL

## Features
- Browse 200,000 products
- Cursor Pagination
- Category filtering
- Search by product name
- Price filtering
- Bulk insert using bulk_create()
- Database indexing

## Why Cursor Pagination?
Offset pagination can duplicate or skip rows when data changes. Cursor pagination ensures stable ordering and fast pagination.

## API Endpoints

GET /api/products/

GET /api/products/?category=Furniture

GET /api/products/?search=chair

GET /api/products/?min_price=1000&max_price=50000

GET /api/products/?category=Furniture&search=chair