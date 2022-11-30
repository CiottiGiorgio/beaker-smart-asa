"""
This file implements the user functions of a Smart ASA.
"""
from beaker import external
from pyteal import Assert, Seq
from pyteal.ast import abi

from beaker_smart_asa.base import BaseSmartASA
from beaker_smart_asa.smart_asa_global_state import SmartASAGlobalState


class SmartASAUser(BaseSmartASA, SmartASAGlobalState):
    """This class implements the user features for a Smart ASA"""

    @external
    def asset_transfer(
        self,
        asa_id: abi.Uint64,
        sender: abi.Address,  # pylint: disable=unused-argument
        receiver: abi.Address,  # pylint: disable=unused-argument
    ):
        """Contract method to transfer the Smart ASA"""
        return Seq(Assert(asa_id.get() == self.UNDERLYING_ASA_ID.get()))
