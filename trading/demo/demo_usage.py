from sdk.client import TradingClient

client = TradingClient("http://127.0.0.1:5000")

client.login("test", "pass")

order = client.place_order(
    symbol="INFY",
    quantity=10,
    side="BUY",
    price=1450
)

print("Order Response:", order)
print("Orders:", client.get_orders())
print("Positions:", client.get_positions())
print("Funds:", client.get_funds())
