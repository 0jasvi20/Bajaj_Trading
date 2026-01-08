import requests
from sdk.exceptions import TradingSDKException


class TradingClient:
    def __init__(self, base_url):
        self.base_url = base_url
        self.token = None

    def login(self, username, password):
        response = requests.post(
            f"{self.base_url}/login",
            json={"username": username, "password": password}
        )

        if response.status_code != 200:
            raise TradingSDKException("Login failed")

        self.token = response.json()["token"]

    def place_order(self, symbol, quantity, side, price):
        if not self.token:
            raise TradingSDKException("User not logged in")

        payload = {
            "symbol": symbol,
            "quantity": quantity,
            "side": side,
            "price": price
        }

        response = requests.post(
            f"{self.base_url}/placeOrder",
            json=payload,
            headers={"Authorization": self.token}
        )

        return response.json()

    def get_orders(self):
        return requests.get(f"{self.base_url}/orders").json()

    def get_positions(self):
        return requests.get(f"{self.base_url}/positions").json()

    def get_funds(self):
        return requests.get(f"{self.base_url}/funds").json()
