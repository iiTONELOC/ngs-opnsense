from .Alias import AliasController


class Firewall:
    """Firewall API class for interacting with OPNSense Firewall API"""

    def __init__(self, url: str, apiKey: str, apiSecret: str) -> None:

        self.apiKey: str = apiKey
        self.apiSecret: str = apiSecret
        self.url: str = f"{url}/firewall"

        self.alias: AliasController = AliasController(
            url=self.url, apiKey=self.apiKey, apiSecret=self.apiSecret
        )
