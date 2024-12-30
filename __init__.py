"""
Copyright (c) 2024 Anthony Tropeano
All Rights Reserved.
"""

from os import environ
from traceback import format_exc

from .Api import CoreAPI
from .helpers import validateParams, _openSenseAPI


class OPNSenseAPI:
    """Class to interact with the OPNSense API

    Args:
        `url (str, optional)`: The URL of the OPNSense instance.
        Defaults to None.
        `apiKey (str, optional)`: The API key for the OPNSense instance.
        Defaults to None.
        `apiSecret (str, optional)`: The API secret for the OPNSense instance.
        Defaults to None.

    Raises:
        `AssertionError`: If the connection to the OPNSense instance fails

    Notes:
        - All endpoints return the response as a JSON string.

        - The url, apiKey, and apiSecret can be provided as arguments or as
          environment variables.

        - The environment variables are: `OPNSENSE_URL`, `OPNSENSE_API_KEY`,
          and `OPNSENSE_API_SECRET`.


    Usage:
       ```python
        import json
        from NG_OPNSense import OPNSenseAPI

        # Create an instance of the OPNSense API
        opnsense = OPNSenseAPI(
            url="https://opnsense.local",
            apiKey="myApiKey",
            apiSecret="myApiSecret")

        # To interact with the OPNSense API, use the same methods provided by
        # the OPNSense API: https://docs.opnsense.org/development/api.html

        # For example, to fetch aliases:
        aliases = opnsense.coreAPI.firewall.alias.get()

        # Print the aliases
        print(json.dumps(aliases, indent=4))
        ```
    """

    def __init__(
        self,
        url: str | None = None,
        apiKey: str | None = None,
        apiSecret: str | None = None,
    ) -> None:
        # Fetch the parameters from the environment if not provided
        url: str = url or environ.get("OPNSENSE_URL")
        apiKey: str = apiKey or environ.get("OPNSENSE_API_KEY")
        apiSecret: str = apiSecret or environ.get("OPNSENSE_API_SECRET")

        # Validate the parameters
        validateParams(url=url, apiKey=apiKey, apiSecret=apiSecret)

        # Set the parameters
        self.url: str = url
        self.apiKey: str = apiKey
        self.apiSecret: str = apiSecret

        #  Verify - Should not be None
        assert self.url is not None
        assert self.apiKey is not None
        assert self.apiSecret is not None

        # Ensure a successful connection
        status: str | None = self.getSystemStatus()
        assert status is not None

        # Attach the CoreAPI
        # https://docs.opnsense.org/development/api.html#core-api
        self.coreAPI = CoreAPI(self.url, self.apiKey, self.apiSecret)

    def getSystemStatus(self) -> str | None:
        """Fetch the system status from the OPNSense API as a JSON string"""
        try:
            url = self.url + "/api/core/system/status"

            response = _openSenseAPI(
                url=url,
                apiKey=self.apiKey,
                apiSecret=self.apiSecret,
            )
            return response.json()
        except Exception:
            print(f"Failed to fetch system status:\n{format_exc()}")
            return None

    def getARPTable(self) -> str | None:
        """Fetch the ARP table from the OPNSense API as a JSON string"""
        try:
            url = self.url + "/api/diagnostics/interface/getArp"

            response = _openSenseAPI(
                url=url,
                apiKey=self.apiKey,
                apiSecret=self.apiSecret,
            )
            return response.json()
        except Exception:
            print(f"Failed to fetch ARP table:\n{format_exc()}")
            return None
