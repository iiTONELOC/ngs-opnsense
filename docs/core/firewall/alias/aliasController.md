# NGS OPNSenseAPI Firewall AliasController

[[&#x2190; Back to Firewall]](../../firewall.md)  
[[&#x2190; Back to README]](../../../../README.md)

## Overview

This module provides a class `AliasController` for interacting with the OPNSense Firewall API to manage aliases. 

Aliases are used in firewall configurations to represent networks, hosts, ports, URLs, etc., in a more manageable way. 

The class supports adding, deleting, searching, and managing alias items, as well as retrieving alias information and mirrors the [OPNSense API](https://docs.opnsense.org/development/api/core/firewall.html).

## API

`/firewall/alias`  
│   ├── /[`addItem`](#additemself-alias-dict---str--none)  
│   ├── /[`delItem`](#delitemself-uuid-str---str--none)  
│   ├── /[`get`](#getself---str--none)  
│   ├── /[`getAliasUUID`](#getaliasuuidself-name-str---str--none)  
│   ├── /[`getGeoIP`](#getgeoipself---str--none)  
│   ├── /[`getItem`](#getitemself-uuid-str---str--none)  
│   ├── /[`getTableSize`](#gettablesizeself---str--none)  
│   ├── /[`listCategories`](#listcategoriesself---str--none)  
│   ├── /[`listCountries`](#listcountriesself---str--none)  
│   ├── /[`listNetworkAliases`](#listnetworkaliasesself---str--none)  
│   ├── /[`listUserGroups`](#listusergroupsself---str--none)  
│   ├── /[`searchItem`](#searchitemself-searchparams-str---str--none)  
│   ├── /[`setItem`](#setitemself-uuid-str-datatoset-dict---str--none)  
│   └── /[`toggleItem`](#toggleitemself-uuid-str-enabled-bool---str--none)  

## Example Usage

```python
# Initialize the AliasController
controller = AliasController(url="https://your-opnsense-url", apiKey="your-api-key", apiSecret="your-api-secret")

# Add an alias
alias_data = {
    "enabled": True,
    "name": "Test Alias",
    "type": "host",
    "proto": ["IPv4"],
    "content": "192.168.1.1",
    "description": "Test description"
}
response = controller.addItem(alias_data)

# Get all aliases
all_aliases = controller.get()

# Delete an alias
response = controller.delItem("alias-uuid")
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

#### `addItem(self, alias: dict) -> str | None`

Adds a new alias to the OPNSense Firewall.

**Arguments**:

- `alias` (dict): A dictionary containing the alias data to be added. The data must conform to the structure described below.

**Returns**:

- `str | None`: The response from the OPNSense Firewall API, or `None` if the request failed.

**Alias Structure**:

The alias data should be structured as follows:

```python
{
    "enabled": bool,
    "name": str,
    "type": AliasType,  # See definitions for available AliasType values
    "proto": Optional[List[ProtoType]],  # Optional,Supported protocols (IPv4, IPv6)
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

---

#### `delItem(self, uuid: str) -> str | None`

Deletes an alias from the OPNSense Firewall using its UUID.

**Arguments**:

- `uuid` (str): The UUID of the alias to delete.

**Returns**:

- `str | None`: The response from the OPNSense Firewall API, or `None` if the request failed.

---

#### `get(self) -> str | None`

Retrieves all aliases from the OPNSense Firewall.

**Returns**:

- `str | None`: The response from the OPNSense Firewall API, or `None` if the request failed.

---

#### `getAliasUUID(self, name: str) -> str | None`

Gets the UUID of an alias based on its name.

**Arguments**:

- `name` (str): The name of the alias.

**Returns**:

- `str | None`: The UUID of the alias, or `None` if the request failed.

---

#### `getGeoIP(self) -> str | None`

Retrieves GeoIP data from the OPNSense Firewall.

**Returns**:

- `str | None`: The response containing GeoIP data, or `None` if the request failed.

---

#### `getItem(self, uuid: str) -> str | None`

Gets a specific alias by its UUID.

**Arguments**:

- `uuid` (str): The UUID of the alias.

**Returns**:

- `str | None`: The response from the OPNSense Firewall API containing the alias data, or `None` if the request failed.

---

#### `getTableSize(self) -> str | None`

Gets the size of the alias table in the OPNSense Firewall.

**Returns**:

- `str | None`: The response containing the table size, or `None` if the request failed.

---

#### `listCategories(self) -> str | None`

Lists the categories of aliases available in the OPNSense Firewall.

**Returns**:

- `str | None`: The response containing alias categories, or `None` if the request failed.

---

#### `listCountries(self) -> str | None`

Lists the countries available in the OPNSense Firewall.

**Returns**:

- `str | None`: The response containing country data, or `None` if the request failed.

---

#### `listNetworkAliases(self) -> str | None`

Lists network aliases available in the OPNSense Firewall.

**Returns**:

- `str | None`: The response containing network alias data, or `None` if the request failed.

---

#### `listUserGroups(self) -> str | None`

Lists user groups available in the OPNSense Firewall.

**Returns**:

- `str | None`: The response containing user group data, or `None` if the request failed.

---

#### `searchItem(self, searchParams: str) -> str | None`

Searches for an alias item using specified search parameters.

**Arguments**:

- `searchParams` (str): The search parameters to use when looking for an alias item.

**Returns**:

- `str | None`: The response containing search results, or `None` if the request failed.

---

#### `setItem(self, uuid: str, dataToSet: dict) -> str | None`

Sets or updates an alias item with new data.

**Arguments**:

- `uuid` (str): The UUID of the alias to update.
- `dataToSet` (dict): The data to set for the alias.

**Returns**:

- `str | None`: The response from the OPNSense Firewall API, or `None` if the request failed.

---

#### `toggleItem(self, uuid: str, enabled: bool) -> str | None`

Toggles the state of an alias (enabled/disabled).

**Arguments**:

- `uuid` (str): The UUID of the alias to toggle.
- `enabled` (bool): The new state to set (True for enabled, False for disabled).

**Returns**:

- `str | None`: The response from the OPNSense Firewall API, or `None` if the request failed.

## Error Handling

If any request to the OPNSense API fails, the respective method will print the exception traceback and return `None`.

---
[[&#x2190; Back to Top]](#ngs-opnsenseapi-firewall-aliascontroller)  
[[&#x2190; Back to Firewall Docs]](../../firewall.md)  
[[&#x2190; Back to README]](../../../../README.md)
