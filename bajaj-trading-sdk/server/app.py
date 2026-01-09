from flask import Flask, request, jsonify
import uuid
from storage import instruments, orders, trades, portfolio

app = Flask(__name__)

# ----------------------------
# ROOT / HEALTH CHECK
# ----------------------------
@app.route("/")
def health():
    return {
        "message": "Bajaj Trading API is running",
        "available_endpoints": [
            "/api/v1/instruments",
            "/api/v1/orders",
            "/api/v1/orders/<orderId>",
            "/api/v1/trades",
            "/api/v1/portfolio"
        ]
    }

# ----------------------------
# 1. Instruments API
# ----------------------------
@app.route("/api/v1/instruments", methods=["GET"])
def get_instruments():
    return jsonify(instruments)

# ----------------------------
# 2. Place Order API
# ----------------------------
@app.route("/api/v1/orders", methods=["POST"])
def place_order():
    data = request.json

    # Validations
    if data.get("quantity", 0) <= 0:
        return {"error": "Quantity must be greater than 0"}, 400

    if data.get("orderStyle") == "LIMIT" and "price" not in data:
        return {"error": "Price required for LIMIT order"}, 400

    order_id = str(uuid.uuid4())[:8]

    order = {
        "orderId": order_id,
        "symbol": data["symbol"],
        "side": data["side"],               # BUY / SELL
        "orderStyle": data["orderStyle"],   # MARKET / LIMIT
        "quantity": data["quantity"],
        "price": data.get("price"),
        "status": "EXECUTED"
    }

    orders[order_id] = order
    trades.append(order)

    qty_change = data["quantity"] if data["side"] == "BUY" else -data["quantity"]
    portfolio[data["symbol"]] = portfolio.get(data["symbol"], 0) + qty_change

    return jsonify(order)

# ----------------------------
# 3. Get Order Status
# ----------------------------
@app.route("/api/v1/orders/<order_id>", methods=["GET"])
def get_order(order_id):
    if order_id not in orders:
        return {"error": "Order not found"}, 404
    return jsonify(orders[order_id])

# ----------------------------
# 4. Trades API
# ----------------------------
@app.route("/api/v1/trades", methods=["GET"])
def get_trades():
    return jsonify(trades)

# ----------------------------
# 5. Portfolio API
# ----------------------------
@app.route("/api/v1/portfolio", methods=["GET"])
def get_portfolio():
    response = []
    for symbol, qty in portfolio.items():
        response.append({
            "symbol": symbol,
            "quantity": qty,
            "averagePrice": 0,
            "currentValue": qty
        })
    return jsonify(response)

if __name__ == "__main__":
    app.run(debug=True)
