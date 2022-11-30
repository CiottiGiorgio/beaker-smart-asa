"""
This file contains global fixtures
"""

import pytest
from algosdk.v2client.algod import AlgodClient  # type: ignore
from beaker import sandbox

ALGOD_CLIENT: AlgodClient = sandbox.get_algod_client()
ACCTS = sandbox.get_accounts()


@pytest.fixture(scope="session", name="algod_client")
def _algod_client():
    return ALGOD_CLIENT


@pytest.fixture(scope="session", name="creator_account")
def _creator_account():
    return ACCTS[0].address, ACCTS[0].private_key, ACCTS[0].signer
