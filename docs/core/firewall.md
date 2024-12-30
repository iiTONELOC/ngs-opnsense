# NGS OPNSenseAPI Firewall

[[&#x2190; Back to Core]](../core.md)  
[[&#x2190; Back to README]](../../README.md)

## Overview

The `Firewall` class provides an interface for interacting with the OPNSense Firewall API. It allows users to interact with various firewall-related functionalities, such as managing aliases, categories, groups, filters, and more.

## API

`/firewall`  
│   ├── /[`alias`](./firewall/alias/aliasController.md)            # Manages firewall aliases  
│   ├── /alias_util       # Utility functions for alias management  
│   ├── /category         # Manages categories of firewall rules  
│   ├── /filter_base      # Base filter management for firewall  
│   ├── /filter           # Manage firewall rules  
│   ├── /filter_util      # Utility functions for firewall rules  
│   ├── /group            # Manages groups of firewall rules  
│   ├── /npt              # Network port translation configuration  
│   ├── /one_to_one       # One-to-one NAT configuration  
│   └── /source_nat       # Source NAT configuration  

## Example Usage

```python
# Initialize the AliasController
firewall = Firewall(url="https://your-opnsense-url", apiKey="your-api-key", apiSecret="your-api-secret")

# Add an alias to the firewall
alias_data = {
    "enabled": True,
    "name": "Test Alias",
    "type": "host",
    "proto": ["IPv4"],
    "content": "192.168.1.1",
    "description": "Test description"
}
response = firewall.alias.addItem(alias_data)

# Get all aliases
all_aliases = firewall.alias.get()

# Delete an alias
response = firewall.alias.delItem("alias-uuid")
```

---

[[&#x2190; Back to Core]](../core.md)  
[[&#x2190; Back to README]](../../README.md)
