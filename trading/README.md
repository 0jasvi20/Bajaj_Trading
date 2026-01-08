# Trading SDK – Python

This project is a simplified Trading SDK that wraps REST APIs of a mock trading platform.

## Features
- Login authentication
- Place Buy/Sell orders
- Fetch orders
- Fetch positions
- Fetch available funds

## Tech Stack
- Python
- Flask (Mock Trading API)
- Requests (SDK HTTP calls)

## How to Run

### Step 1: Install dependencies
pip install -r requirements.txt

### Step 2: Start server
cd server
python app.py

### Step 3: Run demo
cd demo
python demo_usage.py
python -m demo.demo_usage

 % cd ~/Desktop/trading
source .venv/bin/activate