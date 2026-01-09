# Bajaj Broking – Trading SDK Assignment

## Overview
This project simulates a trading backend with REST APIs and a wrapper SDK.
It supports instruments, order placement, trades, and portfolio tracking.

## Tech Stack
- Python
- Flask
- In-memory storage
- REST APIs
- SDK Wrapper

## How to Run
1. Install dependencies  
   pip install -r requirements.txt

2. Start server  
   cd server  
   python app.py

3. Run SDK demo  
   cd demo  
   python demo_usage.py

## APIs
- GET /api/v1/instruments
- POST /api/v1/orders
- GET /api/v1/orders/{orderId}
- GET /api/v1/trades
- GET /api/v1/portfolio

## Assumptions
- Single user (mocked authentication)
- Orders execute immediately
- In-memory data storage
