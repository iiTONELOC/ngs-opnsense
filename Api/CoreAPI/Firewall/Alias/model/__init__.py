from enum import Enum
from typing import List, Optional

from pydantic import BaseModel, Field, field_validator

from .regions import Region, RegionCountries
from NG_OPNSense.validators import PROPERTY_NAME_REGEX


# Enum for Alias Type options
class AliasType(str, Enum):
    host: str = "host"
    network: str = "network"
    port: str = "port"
    url: str = "url"
    urltable: str = "urltable"
    geoip: str = "geoip"
    networkgroup: str = "networkgroup"
    mac: str = "mac"
    asn: str = "asn"
    dynipv6host: str = "dynipv6host"
    openvpngroup: str = "openvpn-group"
    internal: str = "internal"
    external: str = "external"


# Enum for Protocol Options
class ProtoType(str, Enum):
    IPv4: str = "IPv4"
    IPv6: str = "IPv6"


# Alias Item Class
# Describes the structure of available options for an alias item
class AliasItem(BaseModel):
    enabled: int = Field(True, description="Enable the alias")
    name: str
    type: str  # Replace with AliasType if you have it defined elsewhere
    proto: Optional[str] = None  # Optional field for protoco
    interface: Optional[str] = None  # Optional, depending on the alias type
    counters: Optional[int] = None  # Optional field for counters
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
    interface: Optional[str] = None  # Optional, depending on the alias type


# Alias Base Class Options - To view these Go to FireWall -> Aliases -> Add
# from the GUI.


class AliasBaseOptions(BaseModel):
    content: str | List[str]
    description: Optional[str] = None
    categories: Optional[str | List[str]] = None
    enabled: int = Field(True, description="Enable the alias")
    name: str = Field(..., min_length=1, max_length=32, pattern=PROPERTY_NAME_REGEX)


class AliasBaseWStatistics(AliasBaseOptions):
    statistics: Optional[int] = None


class AliasHost(AliasBaseWStatistics):
    type: str = AliasType.host.value


class AliasNetworks(AliasBaseWStatistics):
    type: str = AliasType.network.value


class AliasPort(AliasBaseOptions):
    type: str = AliasType.port.value


class AliasURL(AliasBaseWStatistics):
    type: str = AliasType.url.value


class AliasURLTable(AliasBaseWStatistics):
    type: str = AliasType.urltable.value
    refreshFrequency: Optional[tuple[int, int]] = None  # (days, hours)


class AliasGeoIP(AliasBaseWStatistics):
    type: str = AliasType.geoip.value
    proto: Optional[str] = ""
    content: str


class AliasNetworkGroup(AliasBaseWStatistics):
    type: str = AliasType.networkgroup.value


class AliasMAC(AliasBaseWStatistics):
    type: str = AliasType.mac.value


class AliasBgpASN(AliasBaseWStatistics):
    type: str = AliasType.asn.value
    proto: Optional[str] = ""


class AliasDynIPv6Host(AliasBaseWStatistics):
    type: str = AliasType.dynipv6host.value
    interface: Optional[str] = None


class AliasOpenVPNGroup(AliasBaseWStatistics):
    type: str = AliasType.openvpngroup.value


class AliasInternal(AliasBaseWStatistics):
    type: str = AliasType.internal.value


# only oddball, does not have a content field
class AliasExternal(BaseModel):
    enabled: int = Field(True, description="Enable the alias")
    description: Optional[str] = None
    statistics: Optional[int] = None
    categories: Optional[str | List[str]] = None
    interface: Optional[str] = None  # Optional, depending on the alias type
    name: str = Field(..., min_length=1, max_length=32, pattern=PROPERTY_NAME_REGEX)


class AliasClass(Enum):
    host = AliasHost
    network = AliasNetworks
    port = AliasPort
    url = AliasURL
    urltable = AliasURLTable
    geoip = AliasGeoIP
    networkgroup = AliasNetworkGroup
    mac = AliasMAC
    asn = AliasBgpASN
    dynipv6host = AliasDynIPv6Host
    openvpngroup = AliasOpenVPNGroup
    internal = AliasInternal
    external = AliasExternal
