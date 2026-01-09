import requests

class TradingClient:
    def __init__(self, base_url):
        self.base_url = base_url

    def get_instruments(self):
        return requests.get(
            f"{self.base_url}/api/v1/instruments"
        ).json()

    def place_order(self, payload):
        return requests.post(
            f"{self.base_url}/api/v1/orders",
            json=payload
        ).json()

    def get_order_status(self, order_id):
        return requests.get(
            f"{self.base_url}/api/v1/orders/{order_id}"
        ).json()

    def get_trades(self):
        return requests.get(
            f"{self.base_url}/api/v1/trades"
        ).json()

    def get_portfolio(self):
        return requests.get(
            f"{self.base_url}/api/v1/portfolio"
        ).json()
