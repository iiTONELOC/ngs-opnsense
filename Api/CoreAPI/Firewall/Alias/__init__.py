from json import dumps
from traceback import format_exc
from NG_OPNSense.helpers import _openSenseAPI

from .model import *


class AliasController:
    """Alias API class for interacting with OPNSense Firewall API"""

    def __init__(self, url: str, apiKey: str, apiSecret: str) -> None:
        self.apiKey: str = apiKey
        self.apiSecret: str = apiSecret
        self.url: str = f"{url}/alias"

    def addItem(self, alias: dict) -> dict | None:
        """Add an alias to the OPNSense Firewall

        Args:
            `alias (dict)`: The alias data to add to the OPNSense Firewall
            the alias data should be in the format of the AliasItem class
            and has the following structure:
            ```python

            {
                enabled: bool
                name: str
                type: AliasType # See Definitions below for AliasType and ProtoType
                proto: List[ProtoType]  # Multiple protocols allowed (IPv4, IPv6)
                interface: Optional[str] = None  # Optional, depending on the alias type
                counters: Optional[bool] = None  # Optional field for counters
                updatefreq: Optional[int] = None  # Numeric field for update frequency
                content: Optional[str] = None  # Content associated with the alias
                categories: Optional[List[str]] = None  # Categories for the alias
                description: Optional[str] = None  # Description of the alias
            }

            # Enum for Protocol Options
            class ProtoType(str, Enum):
                IPv4 = "IPv4"
                IPv6 = "IPv6"


            # Enum for Alias Type options
            class AliasType(str, Enum):
                host = "host"
                network = "network"
                port = "port"
                url = "url"
                urltable = "urltable"
                geoip = "geoip"
                networkgroup = "networkgroup"
                mac = "mac"
                asn = "asn"
                dynipv6host = "dynipv6host"
                authgroup = "authgroup"
                internal = "internal"
                external = "external"

            ```

        Returns:
            `dict | None`: The json response from the OPNSense Firewall or None if
            the request failed

        Note:
            The alias data will vary depending on the alias being created and the
            field names literally mimic the GUI. So for example when creating a new alias for
            ports the alias data that would need to be provided would look like the following:

            ```json
                {
                    "enabled": 1,
                    "name": "DNS",
                    "type": "port", # or AliasType.port
                    "content" :"53,853"
                    "description": "Port numbers used for DNS"
                }
            ```
        """
        try:
            url = self.url + "/addItem"
            validatedData = AliasItem(**alias).model_dump_json()

            if validatedData is None:
                return dumps({"error": "Invalid Alias Data"})

            response = _openSenseAPI(
                url=url,
                apiKey=self.apiKey,
                apiSecret=self.apiSecret,
                data=dumps({"alias": alias}),
                Method="POST",
            )

            if response is None:
                raise RuntimeError("Failed to add alias")

            return response.json()
        except Exception:
            print(f"Failed to add alias:\n{format_exc()}")
            return None

    def delItem(self, uuid: str) -> dict | None:
        """Delete an alias from the OPNSense Firewall

        Args:
            `uuid (str)`: The UUID of the alias to delete

        Returns:
             `dict | None`: The json response from the OPNSense Firewall or None if
            the request failed
        """
        try:
            url = f"{self.url}/delItem/{uuid}"
            response = _openSenseAPI(
                url=url,
                apiKey=self.apiKey,
                apiSecret=self.apiSecret,
                Method="POST",
            )
            return response.json()
        except Exception:
            print(f"Failed to delete alias:\n{format_exc()}")
            return None

    def get(self) -> dict | None:
        """Get all aliases from the OPNSense Firewall

        Returns:
            `dict | None`: The json response from the OPNSense Firewall or None if
            the request failed
        """
        try:
            url = f"{self.url}/get"
            response = _openSenseAPI(
                url=url,
                apiKey=self.apiKey,
                apiSecret=self.apiSecret,
                Method="GET",
            )
            return response.json()
        except Exception:
            print(f"Failed to get aliases:\n{format_exc()}")

    def getAliasUUID(self, name: str) -> dict | None:
        """Get an alias UUID from the OPNSense Firewall

        Args:
            `name (str)`: The name of the alias to get

        Returns:
            `dict | None`: The UUID of the alias or None if the request failed
        """
        try:
            url = f"{self.url}/getAliasUUID/{name}"
            response = _openSenseAPI(
                url=url,
                apiKey=self.apiKey,
                apiSecret=self.apiSecret,
                Method="GET",
            )
            return response.json()
        except Exception:
            print(f"Failed to get alias UUID:\n{format_exc()}")
            return None

    def getGeoIP(self) -> dict | None:
        """Get GeoIP data from the OPNSense Firewall

        Returns:
            `dict | None`: The json response from the OPNSense Firewall or None if
            the request failed
        """
        try:
            url = f"{self.url}/getGeoIP"
            response = _openSenseAPI(
                url=url,
                apiKey=self.apiKey,
                apiSecret=self.apiSecret,
                Method="GET",
            )
            return response.json()
        except Exception:
            print(f"Failed to get GeoIP data:\n{format_exc()}")
            return None

    def getItem(self, uuid: str) -> dict | None:
        """Get an alias from the OPNSense Firewall

        Args:
            `uuid (str)`: The UUID of the alias to get

        Returns:
            `dict | None`: The json response from the OPNSense Firewall or None if
            the request failed
        """
        try:
            url = f"{self.url}/getItem/{uuid}"
            response = _openSenseAPI(
                url=url,
                apiKey=self.apiKey,
                apiSecret=self.apiSecret,
                Method="GET",
            )
            return response.json()
        except Exception:
            print(f"Failed to get alias:\n{format_exc()}")
            return None

    def getTableSize(self) -> dict | None:
        """Get the size of the alias table from the OPNSense Firewall

        Returns:
            `dict | None`: The json response from the OPNSense Firewall or None if
            the request failed
        """
        try:
            url = f"{self.url}/getTableSize"
            response = _openSenseAPI(
                url=url,
                apiKey=self.apiKey,
                apiSecret=self.apiSecret,
                Method="GET",
            )
            return response.json()
        except Exception:
            print(f"Failed to get table size:\n{format_exc()}")
            return None

    def listCategories(self) -> dict | None:
        """List alias categories from the OPNSense Firewall

        Returns:
            `dict | None`: The json response from the OPNSense Firewall or None if
            the request failed
        """
        try:
            url = f"{self.url}/listCategories"
            response = _openSenseAPI(
                url=url,
                apiKey=self.apiKey,
                apiSecret=self.apiSecret,
                Method="GET",
            )
            return response.json()
        except Exception:
            print(f"Failed to list categories:\n{format_exc()}")
            return None

    def listCountries(self) -> dict | None:
        """List countries from the OPNSense Firewall

        Returns:
            `dict | None`: The json response from the OPNSense Firewall or None if
            the request failed
        """
        try:
            url = f"{self.url}/listCountries"
            response = _openSenseAPI(
                url=url,
                apiKey=self.apiKey,
                apiSecret=self.apiSecret,
                Method="GET",
            )
            return response.json()
        except Exception:
            print(f"Failed to list countries:\n{format_exc()}")
            return None

    def listNetworkAliases(self) -> dict | None:
        """List network aliases from the OPNSense Firewall

        Returns:
            `dict | None`: The json response from the OPNSense Firewall or None if
            the request failed
        """
        try:
            url = f"{self.url}/listNetworkAliases"
            response = _openSenseAPI(
                url=url,
                apiKey=self.apiKey,
                apiSecret=self.apiSecret,
                Method="GET",
            )
            return response.json()
        except Exception:
            print(f"Failed to list network aliases:\n{format_exc()}")
            return None

    def listUserGroups(self) -> dict | None:
        """List user groups from the OPNSense Firewall

        Returns:
            `dict | None`: The json response from the OPNSense Firewall or None if
            the request failed
        """
        try:
            url = f"{self.url}/listUserGroups"
            response = _openSenseAPI(
                url=url,
                apiKey=self.apiKey,
                apiSecret=self.apiSecret,
                Method="GET",
            )
            return response.json()
        except Exception:
            print(f"Failed to list user groups:\n{format_exc()}")
            return None

    def searchItem(self, searchParams: str) -> dict | None:
        """Search for an alias item in the OPNSense Firewall

        Args:
            `searchParams (str)`: The search parameters to use when searching for the alias item

        Returns:
            `dict | None`: The json response from the OPNSense Firewall or None if
            the request failed
        """
        try:
            url = f"{self.url}/searchItem/{searchParams}"
            response = _openSenseAPI(
                url=url,
                apiKey=self.apiKey,
                apiSecret=self.apiSecret,
                Method="GET",
            )
            return response.json()
        except Exception:
            print(f"Failed to search for alias item:\n{format_exc()}")
            return None

    def setItem(self, uuid: str, dataToSet: dict) -> dict | None:
        """Set an alias item in the OPNSense Firewall

        Args:
            `uuid (str)`: The UUID of the alias to set
            `dataToSet (dict)`: The data to set for the alias

        Returns:
            `dict | None`: The json response from the OPNSense Firewall or None if
            the request failed
        """
        try:
            url = f"{self.url}/setItem/{uuid}"
            response = _openSenseAPI(
                url=url,
                apiKey=self.apiKey,
                apiSecret=self.apiSecret,
                data=dumps(dataToSet),
                Method="POST",
            )
            return response.json()
        except Exception:
            print(f"Failed to set alias item:\n{format_exc()}")
            return None

    def toggleItem(self, uuid: str, enabled: bool) -> dict | None:
        """Toggle an alias item in the OPNSense Firewall

        Args:
            `uuid (str)`: The UUID of the alias to toggle
            `enabled (bool)`: The state to set the alias to

        Returns:
            `dict | None`: The json response from the OPNSense Firewall or None if
            the request failed
        """
        try:
            url = f"{self.url}/toggleItem/{uuid}/{int(enabled)}"
            response = _openSenseAPI(
                url=url,
                apiKey=self.apiKey,
                apiSecret=self.apiSecret,
                Method="POST",
            )
            return response.json()
        except Exception:
            print(f"Failed to toggle alias item:\n{format_exc()}")
            return None
