from sdk.trading_client import TradingClient

client = TradingClient("http://127.0.0.1:5000")

print("Instruments:")
print(client.get_instruments())

order = client.place_order({
    "symbol": "INFY",
    "side": "BUY",
    "orderStyle": "MARKET",
    "quantity": 10
})

print("\nOrder Placed:")
print(order)

print("\nOrder Status:")
print(client.get_order_status(order["orderId"]))

print("\nTrades:")
print(client.get_trades())

print("\nPortfolio:")
print(client.get_portfolio())
