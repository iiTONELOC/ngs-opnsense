# NGS OPNSenseAPI Firewall AliasController

[[&#x2190; Back to Firewall]](../../firewall.md)  
[[&#x2190; Back to README]](../../../../README.md)

## Overview

This module provides a class `AliasController` for interacting with the OPNSense Firewall API to manage aliases. 

Aliases are used in firewall configurations to represent networks, hosts, ports, URLs, etc., in a more manageable way. 

The class supports adding, deleting, searching, and managing alias items, as well as retrieving alias information and mirrors the [OPNSense API](https://docs.opnsense.org/development/api/core/firewall.html).

## API

`/firewall/alias`  
│   ├── /[`addItem`](#additemself-alias-dict---dict--none)  
│   ├── /[`delItem`](#delitemself-uuid-str---dict--none)  
│   ├── /[`get`](#getself---dict--none)  
│   ├── /[`getAliasUUID`](#getaliasuuidself-name-str---dict--none)  
│   ├── /[`getGeoIP`](#getgeoipself---dict--none)  
│   ├── /[`getItem`](#getitemself-uuid-str---dict--none)  
│   ├── /[`getTableSize`](#gettablesizeself---dict--none)  
│   ├── /[`listCategories`](#listcategoriesself---dict--none)  
│   ├── /[`listCountries`](#listcountriesself---dict--none)  
│   ├── /[`listNetworkAliases`](#listnetworkaliasesself---dict--none)  
│   ├── /[`listUserGroups`](#listusergroupsself---dict--none)  
│   ├── /[`searchItem`](#searchitemself-searchparams-str---dict--none)  
│   ├── /[`setItem`](#setitemself-uuid-str-datatoset-dict---dict--none)  
│   └── /[`toggleItem`](#toggleitemself-uuid-str-enabled-bool---dict--none)  

## Example Usage

```python
import json
from NG_OPNSense import OPNSenseAPI

opnsense = OPNSenseAPI(url="https://your-opnsense-url", apiKey="your-api-key", apiSecret="your-api-secret")

# Add an alias
aliasData = {
    "enabled": 1,
    "name": "Test Alias",
    "type": "host",
    "proto": "IPv4",
    "content": "192.168.1.1",
    "description": "Test description"
}

# Get the response
response = opnsense.coreAPI.firewall.alias.addItem(aliasData)

print(json.dumps(response,indent=4))
```

## AliasController Class

The `AliasController` class allows interaction with the OPNSense Firewall API specifically for managing aliases. It includes methods for adding, deleting, and fetching aliases, as well as more advanced operations like toggling alias states and working with GeoIP data.

### Constructor: `__init__(self, url: str, apiKey: str, apiSecret: str) -> None`

The constructor initializes the controller with the necessary parameters to communicate with the OPNSense API.

**Arguments**:

- `url` (str): The base URL of the OPNSense Firewall.
- `apiKey` (str): The API key used for authentication.
- `apiSecret` (str): The API secret used for authentication.

### Methods

---

#### `addItem(self, alias: dict) -> dict | None`

Adds a new alias to the OPNSense Firewall.

**Arguments**:

- `alias` (dict): A dictionary containing the alias data to be added. The data must conform to the structure described below.

**Returns**:

- `dict | None`: The response from the OPNSense Firewall API, or `None` if the request failed.

**Alias Structure**:

The alias data should be structured as follows:

```python
{
    "enabled": bool,
    "name": str,
    "type": AliasType,  # See definitions for available AliasType values
    "proto": Optional[str],  # Optional,Supported protocols (IPv4, IPv6)
    "interface": Optional[str] = None,  # Optional, depending on alias type
    "counters": Optional[bool] = None,  # Optional field for counters
    "updatefreq": Optional[int] = None,  # Optional update frequency
    "content": Optional[str] = None,  # Content related to the alias
    "categories": Optional[List[str]] = None,  # Categories for alias
    "description": Optional[str] = None  # Optional description of alias
}
```

**AliasType Enum**:

- `host`
- `network`
- `port`
- `url`
- `urltable`
- `geoip`
- `networkgroup`
- `mac`
- `asn`
- `dynipv6host`
- `authgroup`
- `internal`
- `external`

**ProtoType Enum**:

- `IPv4`
- `IPv6`

##### Adding a Specific Alias Type

While the function validates the type of data being passed in the dictionary, it is validating the data for all types of scenarios. To be sure that the dictionary provided contains valid data for adding a 'host' or 'network' alias, **_model_** classes have been created.

> **_Note_**: Using the Alias models is not a requirement, it is for data validation purposes only. If the dictionary data being passed to the `addItem` function meets the requirements to successfully create the corresponding alias class and has the correct type, i.e. host, port, network etc., then the data can be safely passed instead.

Import the controller:

```python
# Intended use-case is from the OPNSenseAPI
from NG_OPNSense import OPNSenseAPI

# Instantiate a new instance of the OPNSenseAPI
opnsense = OPNSenseAPI(url="https://your-opnsense-url", apiKey="your-api-key", apiSecret="your-api-secret")

# access the controller for the alias
controller = opnsense.coreAPI.firewall.alias
```

**Tested Models**:

- `AliasHost`:

  ```python
  # Class definition
    class AliasHost():
        content:str
        type:Literal["host"]
        enabled: bool/int # use a 1 or 0
        name:str # 1-32 chars must match r"^[a-zA-Z_][a-zA-Z0-9_]*$"
        description: Optional[str] = None
        categories: Optional[str] = None
        statistics: Optional[bool/int] # use a 1 or 0

  ```

  - Example: Create a named alias for the host 192.168.1.175

    ```python
        import json
        from NG_OPNSense.Api.CoreAPI.Firewall.Alias import AliasHost

        # Add host alias to the OPNSense Firewall
        # Example only, use with try/except for error handling
        addedResponse = controller.addItem(
            AliasHost(**{
                "enabled": 0,
                "name": "testAliasHost",
                "content": "192.168.1.175",
            }).model_dump()
        )
     
        print(json.dumps(addedResponse, indent=4))
        # expected output
        """
        {
            "result": "saved",
            "uuid": "<generated_uuid>"
        }
        """
    ```

- `AliasNetworks`:

  ```python
  # Class definition
    class AliasNetworks():
        content:str
        type:Literal["network"]
        enabled: bool/int # use a 1 or 0
        name:str # 1-32 chars must match r"^[a-zA-Z_][a-zA-Z0-9_]*$"
        description: Optional[str] = None
        categories: Optional[str] = None
        statistics: Optional[bool/int] # use a 1 or 0

  ```

  - Example: Create a named alias for the 192.168.0.1 network

    ```python
        import json
        from NG_OPNSense.Api.CoreAPI.Firewall.Alias import AliasNetworks

        # Add network alias to the OPNSense Firewall
        # Example only, use with try/except for error handling
        addedResponse = controller.addItem(
            AliasNetworks(**{
                "enabled": 0,
                "name": "testAliasNetworks",
                "content": "192.168.0.1",
            }).model_dump()
        )

        print(json.dumps(addedResponse, indent=4))
        # expected output
        """
        {
            "result": "saved",
            "uuid": "<generated_uuid>"
        }
        """
    ```

- `AliasPort`:

  ```python
  # Class definition
    class AliasPort():
        content:str 
        type:Literal["port"]
        enabled: bool/int # use a 1 or 0
        name:str # 1-32 chars must match r"^[a-zA-Z_][a-zA-Z0-9_]*$"
        description: Optional[str] = None
        categories: Optional[str] = None

  ```

  - Example: Create a Ports Alias for HTTP and HTTPS

    ```python
        import json
        from NG_OPNSense.Api.CoreAPI.Firewall.Alias import AliasPort

        # Add port alias to the OPNSense Firewall
        # Example only, use with try/except for error handling
        addedResponse = controller.addItem(
            AliasPort(**{
                "enabled": 0,
                "name": "HTTP_S",
                "content": "80, 443",
            }).model_dump()
        )

        print(json.dumps(addedResponse, indent=4))
        # expected output
        """
        {
            "result": "saved",
            "uuid": "<generated_uuid>"
        }
        """
    ```

- `AliasURL`:

  ```python
  # Class definition
    class AliasURL():
        content:str
        type:Literal["url"]
        enabled: bool/int # use a 1 or 0
        name:str # 1-32 chars must match r"^[a-zA-Z_][a-zA-Z0-9_]*$"
        description: Optional[str] = None
        categories: Optional[str] = None
        statistics: Optional[bool/int] # use a 1 or 0

  ```

  - Example: Create a URL Alias for Google

    ```python
        import json
        from NG_OPNSense.Api.CoreAPI.Firewall.Alias import AliasURL

        # Add url alias to the OPNSense Firewall
        # Example only, use with try/except for error handling
        addedResponse = controller.addItem(
            AliasURL(**{
                "enabled": 0,
                "name": "Google",
                "content": "https://www.google.com",
            }).model_dump()
        )
       
        print(json.dumps(addedResponse, indent=4))
        # expected output
        """
        {
            "result": "saved",
            "uuid": "<generated_uuid>"
        }
        """
    ```

- `AliasURLTable`:

  ```python
  # Class definition
    class AliasURLTable():
        content:str
        type:Literal["urltable"]
        enabled: bool/int # use a 1 or 0
        name:str # 1-32 chars must match r"^[a-zA-Z_][a-zA-Z0-9_]*$"
        description: Optional[str] = None
        categories: Optional[str] = None
        statistics: Optional[bool/int] # use a 1 or 0

  ```

  - Example: Create a URL Table - Noted this isn't a great example but the input is accepted

    ```python
        import json
        from NG_OPNSense.Api.CoreAPI.Firewall.Alias import AliasURLTable

        # Add urltables alias to the OPNSense Firewall
        # Example only, use with try/except for error handling
        addedResponse = controller.addItem(
            AliasURLTable(**{
                "enabled": 0,
                "name": "badExample",
                "content": "https://www.google.com",
            }).model_dump()
        )
        
        print(json.dumps(addedResponse, indent=4))
        # expected output
        """
        {
            "result": "saved",
            "uuid": "<generated_uuid>"
        }
        """
    ```

- `AliasGeoIP`:

  ```python
  # Class definition
    class AliasGeoIP():
        content:str # newline separated country codes 
        type:Literal["geoip"]
        enabled: bool/int # use a 1 or 0
        name:str # 1-32 chars must match r"^[a-zA-Z_][a-zA-Z0-9_]*$"
        proto: Optional[str] = ""
        description: Optional[str] = None
        categories: Optional[str] = None
        statistics: Optional[bool/int] # use a 1 or 0

  ```

  - Example: Create a GeoIP Alias for the United States, Canada, and Mexico

    ```python
        import json
        # a dictionary of Regions, containing dictionaries of countries, and 
        # their country codes is available if needed
        from NG_OPNSense.Api.CoreAPI.Firewall.Alias import AliasGeoIP, RegionCountries
  
        # Add a GeoIP alias to the OPNSense Firewall
        # Example only, use with try/except for error handling
        addedResponse = controller.addItem(
            AliasGeoIP(**{
            "enabled": 0,
            "name": "NorthAmerica",
            "proto": "",
            # If the codes are known -  "US\nMX\nCA"
            "content": "\n".join([RegionCountries["America"]["United States"], 
                            RegionCountries["America"]["Mexico"], 
                            RegionCountries["America"]["Canada"]])
        }).model_dump()
        )

        print(json.dumps(addedResponse, indent=4))
        # expected output
        """
        {
            "result": "saved",
            "uuid": "<generated_uuid>"
        }
        """
    ```

- `AliasNetworkGroup`:

  ```python
  # Class definition
    class AliasNetworkGroup():
        content:str
        type:Literal["networkgroup"]
        enabled: bool/int # use a 1 or 0
        name:str # 1-32 chars must match r"^[a-zA-Z_][a-zA-Z0-9_]*$"
        proto: Optional[str] = ""
        description: Optional[str] = None
        categories: Optional[str] = None
        statistics: Optional[bool/int] # use a 1 or 0

  ```

  - Example: Create a network group Alias

    ```python
        import json
        from NG_OPNSense.Api.CoreAPI.Firewall.Alias import AliasNetworkGroup        

        # Add a network group alias to the OPNSense Firewall
        # Example only, use with try/except for error handling
        addedResponse = controller.addItem(
            AliasNetworkGroup(**{
            "enabled": 0,
            "name": "testAliasNetworkGroup",
            "proto": "",
            "content": "__lan_network",
        }).model_dump()
        )
       
        print(json.dumps(addedResponse, indent=4))
        # expected output
        """
        {
            "result": "saved",
            "uuid": "<generated_uuid>"
        }
        """
    ```

- `AliasMAC`:

  ```python
  # Class definition
    class AliasMac():
        content:str 
        type:Literal["mac"]
        enabled: bool/int # use a 1 or 0
        name:str # 1-32 chars must match r"^[a-zA-Z_][a-zA-Z0-9_]*$"
        proto: Optional[str] = ""
        description: Optional[str] = None
        categories: Optional[str] = None
        statistics: Optional[bool/int] # use a 1 or 0

  ```

  - Example: Create a mac address alias

    ```python
        import json
        from NG_OPNSense.Api.CoreAPI.Firewall.Alias import AliasMac

        # Add a mac alias to the OPNSense Firewall
        # Example only, use with try/except for error handling
        addedResponse = controller.addItem(
            AliasMac(**{
            "enabled": 0,
            "name": "testAliasMAC",
            "content": "00:00:00:00:00:00",
        }).model_dump()
        )

        print(json.dumps(addedResponse, indent=4))
        # expected output
        """
        {
            "result": "saved",
            "uuid": "<generated_uuid>"
        }
        """
    ```

- `AliasBgpASN`:

  ```python
  # Class definition
    class AliasBgpASN():
        content:str 
        type:Literal["asn"]
        enabled: bool/int # use a 1 or 0
        name:str # 1-32 chars must match r"^[a-zA-Z_][a-zA-Z0-9_]*$"
        proto: Optional[str] = ""
        description: Optional[str] = None
        categories: Optional[str] = None
        statistics: Optional[bool/int] # use a 1 or 0

  ```

  - Example: Create a BGP ASN Alias

    ```python
        import json
        from NG_OPNSense.Api.CoreAPI.Firewall.Alias import AliasBgpASN

        # Add a BGP ASN alias to the OPNSense Firewall
        # Example only, use with try/except for error handling
        addedResponse = controller.addItem(
            AliasBgpASN(**{
            "enabled": 0,
            "name": "testAliasBgpASN",
            "content": "12345",
        }).model_dump()
        )

        print(json.dumps(addedResponse, indent=4))
        # expected output
        """
        {
            "result": "saved",
            "uuid": "<generated_uuid>"
        }
        """
    ```

---

#### `delItem(self, uuid: str) -> dict | None`

Deletes an alias from the OPNSense Firewall using its UUID.

**Arguments**:

- `uuid` (str): The UUID of the alias to delete.

**Returns**:

- `dict | None`: The response from the OPNSense Firewall API, or `None` if the request failed.

---

#### `get(self) -> dict | None`

Retrieves all aliases from the OPNSense Firewall.

**Returns**:

- `dict | None`: The response from the OPNSense Firewall API, or `None` if the request failed.

---

#### `getAliasUUID(self, name: str) -> dict | None`

Gets the UUID of an alias based on its name.

**Arguments**:

- `name` (str): The name of the alias.

**Returns**:

- `dict | None`: The UUID of the alias, or `None` if the request failed.

---

#### `getGeoIP(self) -> dict | None`

Retrieves GeoIP data from the OPNSense Firewall.

**Returns**:

- `dict | None`: The response containing GeoIP data, or `None` if the request failed.

---

#### `getItem(self, uuid: str) -> dict | None`

Gets a specific alias by its UUID.

**Arguments**:

- `uuid` (str): The UUID of the alias.

**Returns**:

- `dict | None`: The response from the OPNSense Firewall API containing the alias data, or `None` if the request failed.

---

#### `getTableSize(self) -> dict | None`

Gets the size of the alias table in the OPNSense Firewall.

**Returns**:

- `dict | None`: The response containing the table size, or `None` if the request failed.

---

#### `listCategories(self) -> dict | None`

Lists the categories of aliases available in the OPNSense Firewall.

**Returns**:

- `dict | None`: The response containing alias categories, or `None` if the request failed.

---

#### `listCountries(self) -> dict | None`

Lists the countries available in the OPNSense Firewall.

**Returns**:

- `dict | None`: The response containing country data, or `None` if the request failed.

---

#### `listNetworkAliases(self) -> dict | None`

Lists network aliases available in the OPNSense Firewall.

**Returns**:

- `dict | None`: The response containing network alias data, or `None` if the request failed.

---

#### `listUserGroups(self) -> dict | None`

Lists user groups available in the OPNSense Firewall.

**Returns**:

- `dict | None`: The response containing user group data, or `None` if the request failed.

---

#### `searchItem(self, searchParams: str) -> dict | None`

Searches for an alias item using specified search parameters.

**Arguments**:

- `searchParams` (str): The search parameters to use when looking for an alias item.

**Returns**:

- `dict | None`: The response containing search results, or `None` if the request failed.

---

#### `setItem(self, uuid: str, dataToSet: dict) -> dict | None`

Sets or updates an alias item with new data.

**Arguments**:

- `uuid` (str): The UUID of the alias to update.
- `dataToSet` (dict): The data to set for the alias.

**Returns**:

- `dict | None`: The response from the OPNSense Firewall API, or `None` if the request failed.

---

#### `toggleItem(self, uuid: str, enabled: bool) -> dict | None`

Toggles the state of an alias (enabled/disabled).

**Arguments**:

- `uuid` (str): The UUID of the alias to toggle.
- `enabled` (bool): The new state to set (True for enabled, False for disabled).

**Returns**:

- `dict | None`: The response from the OPNSense Firewall API, or `None` if the request failed.

## Error Handling

If any request to the OPNSense API fails, the respective method will print the exception traceback and return `None`.

---
[[&#x2190; Back to Top]](#ngs-opnsenseapi-firewall-aliascontroller)  
[[&#x2190; Back to Firewall Docs]](../../firewall.md)  
[[&#x2190; Back to README]](../../../../README.md)
