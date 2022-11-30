"""
This file contains tests for Smart ASA.
"""


import logging

from beaker import client

from beaker_smart_asa.smart_asa import SmartASA


def test_asset_create(algod_client, creator_account):
    """Tests the creation of the Smart ASA"""
    logger = logging.getLogger()

    contract = SmartASA()
    creator, _, signer = creator_account

    app_client = client.ApplicationClient(algod_client, contract, signer=signer)

    app_id, _, _ = app_client.create()
    logger.info("app_id=%s", app_id)

    app_client.fund(200_000)

    suggested_params = algod_client.suggested_params()
    suggested_params.fee = suggested_params.min_fee * 2
    underlying_asa_id = app_client.call(
        SmartASA.asset_create,
        total=1000,
        decimals=0,
        default_frozen=False,
        unit_name="TEST",
        name="Test",
        url="",
        metadata_hash=bytearray(32),
        manager_addr=creator,
        reserve_addr=creator,
        freeze_addr=creator,
        clawback_addr=creator,
        suggested_params=suggested_params,
    )

    logger.info("underlying_asa_id=%s", underlying_asa_id.return_value)
