import os
import pytest
from json import dumps

from NG_OPNSense.Api.CoreAPI.Firewall.Alias import (
    AliasController,
    AliasType,
    AliasHost,
    AliasNetworks,
    AliasPort,
    AliasURL,
    AliasURLTable,
    AliasGeoIP,
    AliasNetworkGroup,
    AliasMAC,
    AliasBgpASN,
    AliasClass,
    # Not Currently tested
    AliasDynIPv6Host,
    AliasOpenVPNGroup,
    AliasInternal,
    AliasExternal,
    # Not Currently tested
)

alias = None
addedAliasId = None
addPortData: dict[str, int | str | AliasType] = {
    "enabled": 0,
    "name": "testAlias",
    "type": AliasType.port.value,
    "content": "80",
    "description": "Test Alias",
}
addAliasTestData: dict[str, AliasClass] = {
    "AliasHost": AliasHost(
        **{
            "enabled": 0,
            "name": "testAliasHost",
            "content": "0.0.0.0",
        }
    ),
    "AliasNetworks": AliasNetworks(
        **{
            "enabled": 0,
            "name": "testAliasNet",
            "content": "192.168.0.1",
        }
    ),
    "AliasPort": AliasPort(
        **{
            "enabled": 0,
            "name": "testAliasPort",
            "content": "80",
        }
    ),
    "AliasURL": AliasURL(
        **{
            "enabled": 0,
            "name": "testAliasURL",
            "content": "https://www.google.com",
        }
    ),
    "AliasURLTable": AliasURLTable(
        **{
            "enabled": 0,
            "name": "testAliasURLTable",
            "content": "https://www.google.com",
        }
    ),
    "AliasGeoIP": AliasGeoIP(
        **{
            "enabled": 0,
            "name": "testAliasGeoIP",
            "proto": "",
            "content": "US\nCA\nMX",
        }
    ),
    "AliasNetworkGroup": AliasNetworkGroup(
        **{
            "enabled": 0,
            "name": "testAliasNetworkGroup",
            "content": "__lan_network",
        }
    ),
    "AliasMAC": AliasMAC(
        **{
            "enabled": 0,
            "name": "testAliasMAC",
            "content": "00:00:00:00:00:00",
        }
    ),
    "AliasBgpASN": AliasBgpASN(
        **{
            "enabled": 0,
            "name": "testAliasBgpASN",
            "content": "12345",
        }
    ),
}


def test_Alias() -> None:
    """Tests AliasController instantiation"""
    global alias

    url: str | None = os.getenv("OPNSENSE_URL_TEST")
    apiKey: str | None = os.getenv("OPNSENSE_API_KEY_TEST")
    apiSecret: str | None = os.getenv("OPNSENSE_API_SECRET_TEST")
    if url is None or apiKey is None or apiSecret is None:
        # throw error
        pytest.fail(
            "Test Environment variables not set!\n"
            "Ensure the following environment variables are set:\n"
            "OPNSENSE_URL_TEST, OPNSENSE_API_KEY_TEST, OPNSENSE_API_SECRET_TEST"
        )

    alias = AliasController(
        url=os.getenv("OPNSENSE_URL_TEST") + "/api/firewall",
        apiKey=os.getenv("OPNSENSE_API_KEY_TEST"),
        apiSecret=os.getenv("OPNSENSE_API_SECRET_TEST"),
    )

    assert all(
        getattr(alias, method) is not None
        for method in [
            "addItem",
            "delItem",
            "getItem",
            "get",
            "getAliasUUID",
            "getGeoIP",
            "getTableSize",
            "listCategories",
            "listCountries",
            "listNetworkAliases",
            "listUserGroups",
            "searchItem",
            "setItem",
            "toggleItem",
        ]
    )


def test_addItem() -> None:
    while alias is None:
        continue

    data: dict | None = alias.addItem(addPortData)

    assert data is not None
    assert data["result"] == "saved"

    global addedAliasId
    addedAliasId = data["uuid"]


def test_addAliases() -> None:
    for _, aliasData in addAliasTestData.items():

        data: dict | None = alias.addItem(aliasData.model_dump())
        if data is None or data["result"] != "saved":
            print(f"Failed to add {aliasData.__class__.__name__}")
            print(aliasData.model_dump())
            print()
            print(data)
        assert data is not None
        assert data["result"] == "saved"

        alias.delItem(uuid=data["uuid"])


def test_getItem() -> None:
    while alias is None or addedAliasId is None:
        continue

    assert addedAliasId is not None

    data: dict | None = alias.getItem(uuid=addedAliasId)

    assert data is not None
    assert data["alias"]["name"] == "testAlias"


def test_get() -> None:
    while alias is None:
        continue

    firewallAliases: dict | None = alias.get()

    assert firewallAliases is not None
    assert "testAlias" in dumps(firewallAliases["alias"]["aliases"])


def test_getAliasUUID() -> None:
    while alias is None:
        continue

    data: dict | None = alias.getAliasUUID(name=addPortData["name"])

    assert data is not None
    assert data["uuid"] == addedAliasId


def test_delItem() -> None:
    global addedAlias
    while alias is None or addedAliasId is None:
        continue

    assert addedAliasId is not None

    data: dict | None = alias.delItem(uuid=addedAliasId)

    assert data is not None
    assert data["result"] == "deleted"

    addedAlias = None
