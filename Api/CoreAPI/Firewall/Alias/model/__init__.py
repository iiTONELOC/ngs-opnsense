from enum import Enum
from typing import List, Optional, Literal

from pydantic import BaseModel, Field, field_validator

from .regions import Region, RegionCountries
from NG_OPNSense.validators import (
    PROPERTY_NAME_REGEX,
    REGION_COUNTRY_CODE_LIST_REGEX,
)

ENABLE_THE_ALIAS = "Enable the alias"


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
    enabled: int = Field(True, description=ENABLE_THE_ALIAS)
    name: str
    type: str  # Replace with AliasType if you have it defined elsewhere
    proto: Optional[str] = None  # Optional field for protoco
    interface: Optional[str] = None  # Optional, depending on the alias type
    counters: Optional[int] = None  # Optional field for counters
    updatefreq: Optional[int] = None  # Numeric field for update frequency
    content: Optional[str] = None  # Content associated with the alias
    categories: Optional[str] = None  # Categories for the alias
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
    content: str
    description: Optional[str] = None
    categories: Optional[str] = None
    enabled: int = Field(True, description=ENABLE_THE_ALIAS)
    name: str = Field(..., min_length=1, max_length=32, pattern=PROPERTY_NAME_REGEX)


class AliasBaseWStatistics(AliasBaseOptions):
    statistics: Optional[int] = None


class AliasHost(AliasBaseWStatistics):
    type: Literal["host"] = "host"


class AliasNetworks(AliasBaseWStatistics):
    type: Literal["network"] = "network"


class AliasPort(AliasBaseOptions):
    type: Literal["port"] = "port"


class AliasURL(AliasBaseWStatistics):
    type: Literal["url"] = "url"


class AliasURLTable(AliasBaseWStatistics):
    type: Literal["urltable"] = "urltable"
    refreshFrequency: Optional[tuple[int, int]] = None  # (days, hours)


class AliasGeoIP(AliasBaseWStatistics):
    type: Literal["geoip"] = "geoip"
    proto: Optional[str] = ""
    content: str = Field(..., pattern=REGION_COUNTRY_CODE_LIST_REGEX)

    @field_validator("content")
    def validate_content(cls, v):
        valid_codes = [
            country_code
            for country in RegionCountries.values()
            for country_code in country.values()
        ]
        codes = v.split("\n")
        for code in codes:
            if code not in valid_codes:
                raise ValueError(f"{code} is not a valid country code.")
        return v


class AliasNetworkGroup(AliasBaseWStatistics):
    type: Literal["networkgroup"] = "networkgroup"


class AliasMAC(AliasBaseWStatistics):
    type: Literal["mac"] = "mac"


class AliasBgpASN(AliasBaseWStatistics):
    type: Literal["asn"] = "asn"
    proto: Optional[str] = ""


class AliasDynIPv6Host(AliasBaseWStatistics):
    type: Literal["dynipv6host"] = "dynipv6host"
    interface: Optional[str] = None


class AliasOpenVPNGroup(AliasBaseWStatistics):
    type: Literal["openvpngroup"] = "openvpngroup"


class AliasInternal(AliasBaseWStatistics):
    type: Literal["internal"] = "internal"


# only oddball, does not have a content field
class AliasExternal(BaseModel):
    enabled: int = Field(True, description=ENABLE_THE_ALIAS)
    description: Optional[str] = None
    statistics: Optional[int] = None
    categories: Optional[str] = None
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
