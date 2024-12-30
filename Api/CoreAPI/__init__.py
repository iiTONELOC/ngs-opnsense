from .Firewall import Firewall


class CoreAPI:
    """Main API class for interacting with OPNSense API"""

    def __init__(self, url: str, apiKey: str, apiSecret: str) -> None:

        self.apiKey: str = apiKey
        self.url: str = f"{url}/api"
        self.apiSecret: str = apiSecret

        self.firewall = Firewall(self.url, self.apiKey, self.apiSecret)
