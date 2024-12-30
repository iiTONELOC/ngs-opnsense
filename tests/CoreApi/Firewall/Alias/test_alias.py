import os
import pytest
from NG_OPNSense.Api.CoreAPI.Firewall.Alias import AliasController, AliasType


def test_Alias():
    alias = AliasController(
        url=os.getenv("OPNSENSE_URL") + "/api/firewall",
        apiKey=os.getenv("OPNSENSE_API_KEY"),
        apiSecret=os.getenv("OPNSENSE_API_SECRET"),
    )
    assert alias.addItem is not None
    assert alias.delItem is not None

    def test_addItem():
        aliasData = {
            "enabled": 0,
            "name": "testAlias",
            "type": AliasType.port,
            "content": "80",
            "description": "Test Alias",
        }

        data = alias.addItem(aliasData)
        assert data is not None
        assert data["result"] == "saved"
        return data

    def test_getItem(id):
        assert id is not None
        data = alias.getItem(id)
        assert data is not None
        assert data["alias"]["name"] == "testAlias"

    def test_delItem(id):
        assert id is not None
        data = alias.delItem(id)
        assert data is not None
        assert data["result"] == "deleted"

    data = test_addItem()
    test_getItem(data["uuid"])
    test_delItem(data["uuid"])
