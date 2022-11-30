"""
This file implements the manager functions of a Smart ASA.
"""
from typing import Literal

from beaker import Authorize, external
from pyteal import Bytes, Global, InnerTxn, InnerTxnBuilder, Int, Seq, TxnField, TxnType
from pyteal.ast import abi

from beaker_smart_asa.base import BaseSmartASA
from beaker_smart_asa.smart_asa_global_state import SmartASAGlobalState


class SmartASAManager(BaseSmartASA, SmartASAGlobalState):
    """This class implements the manager features for a Smart ASA"""

    @external(authorize=Authorize.only(Global.creator_address()))
    def asset_create(  # pylint: disable=too-many-arguments
        self,
        total: abi.Uint64,
        decimals: abi.Uint32,
        default_frozen: abi.Bool,
        unit_name: abi.String,
        name: abi.String,
        url: abi.String,
        metadata_hash: abi.StaticArray[abi.Byte, Literal[32]],
        # metadata_hash: abi.DynamicArray[abi.Byte],
        manager_addr: abi.Address,
        reserve_addr: abi.Address,
        freeze_addr: abi.Address,
        clawback_addr: abi.Address,
        *,
        output: abi.Uint64
    ):
        """Contract method to create the Smart ASA"""
        return Seq(
            SmartASAManager.TOTAL.set(total.get()),
            SmartASAManager.DECIMALS.set(decimals.get()),
            SmartASAManager.DEFAULT_FROZEN.set(default_frozen.get()),
            SmartASAManager.UNIT_NAME.set(unit_name.get()),
            SmartASAManager.NAME.set(name.get()),
            SmartASAManager.URL.set(url.get()),
            SmartASAManager.METADATA_HASH.set(metadata_hash.encode()),
            SmartASAManager.MANAGER_ADDR.set(manager_addr.get()),
            SmartASAManager.RESERVE_ADDR.set(reserve_addr.get()),
            SmartASAManager.FREEZE_ADDR.set(freeze_addr.get()),
            SmartASAManager.CLAWBACK_ADDR.set(clawback_addr.get()),
            InnerTxnBuilder.Begin(),
            InnerTxnBuilder.SetFields(
                {
                    TxnField.fee: Int(0),
                    TxnField.type_enum: TxnType.AssetConfig,
                    TxnField.config_asset_total: Int(2**64 - 1),
                    TxnField.config_asset_decimals: decimals.get(),
                    TxnField.config_asset_default_frozen: Int(1),
                    TxnField.config_asset_unit_name: Bytes("S-ASA"),
                    TxnField.config_asset_name: Bytes("SMART-ASA"),
                    TxnField.config_asset_url: url.get(),
                    TxnField.config_asset_manager: Global.creator_address(),
                    TxnField.config_asset_reserve: Global.creator_address(),
                    TxnField.config_asset_freeze: Global.creator_address(),
                    TxnField.config_asset_clawback: Global.creator_address(),
                }
            ),
            InnerTxnBuilder.Submit(),
            output.set(InnerTxn.created_asset_id()),
        )
