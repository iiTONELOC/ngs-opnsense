from enum import Enum
from typing import List, Optional

from pydantic import BaseModel, Field, field_validator


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


# Enum for Protocol Options
class ProtoType(str, Enum):
    IPv4 = "IPv4"
    IPv6 = "IPv6"


# Alias Item Class
class AliasItem(BaseModel):
    enabled: bool = Field(True, description="Enable the alias")
    name: str
    type: str  # Replace with AliasType if you have it defined elsewhere
    proto: Optional[List[str]] = None  # Replace with ProtoType if applicable
    interface: Optional[str] = None  # Optional, depending on the alias type
    counters: Optional[bool] = None  # Optional field for counters
    updatefreq: Optional[int] = None  # Numeric field for update frequency
    content: Optional[str] = None  # Content associated with the alias
    categories: Optional[List[str]] = None  # Categories for the alias
    description: Optional[str] = None  # Description of the alias

    # Validation to ensure updatefreq is numeric if provided
    @field_validator("updatefreq")
    def validate_updatefreq(cls, v):
        if v is not None and not isinstance(v, int):
            raise ValueError("updatefreq should be a numeric value or left empty.")
        return v


# GeoIP structure (simplified as URL Field)
class GeoIP(BaseModel):
    url: str  # Placeholder field for GeoIP URL


# Full Model for the Aliases (containing items)
class AliasModel(BaseModel):
    geoip: Optional[GeoIP] = None
    aliases: List[AliasItem]
