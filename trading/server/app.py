from flask import Flask, request, jsonify
from data import users, orders, positions
import uuid

app = Flask(__name__)


@app.route("/")
def home():
    return jsonify({
        "message": "Trading API is running successfully",
        "endpoints": {
            "POST /login": "Login user",
            "POST /placeOrder": "Place BUY/SELL order",
            "GET /orders": "Get all orders",
            "GET /positions": "Get current positions",
            "GET /funds": "Get available funds"
        }
    })


@app.route("/login", methods=["POST"])
def login():
    data = request.json
    username = data.get("username")
    password = data.get("password")

    if username in users and users[username]["password"] == password:
        return jsonify({"token": f"TOKEN-{username}"})

    return jsonify({"error": "Invalid credentials"}), 401


@app.route("/placeOrder", methods=["POST"])
def place_order():
    data = request.json

    order_id = str(uuid.uuid4())[:8]

    order = {
        "order_id": order_id,
        "symbol": data["symbol"],
        "quantity": data["quantity"],
        "side": data["side"],
        "price": data["price"],
        "status": "EXECUTED"
    }

    orders.append(order)

    symbol = data["symbol"]
    qty = data["quantity"] if data["side"] == "BUY" else -data["quantity"]
    positions[symbol] = positions.get(symbol, 0) + qty

    return jsonify({
        "message": "Order placed successfully",
        "order_id": order_id
    })


@app.route("/orders", methods=["GET"])
def get_orders():
    return jsonify(orders)


@app.route("/positions", methods=["GET"])
def get_positions():
    return jsonify(positions)


@app.route("/funds", methods=["GET"])
def get_funds():
    return jsonify({
        "available_balance": users["test"]["balance"]
    })


if __name__ == "__main__":
    app.run(debug=True)
