"""
This file implements the global storage of a Smart ASA.
"""

from typing import Final

from beaker import ApplicationStateValue
from pyteal import TealType


class SmartASAGlobalState:
    """This class hold the global state for Smart ASA"""

    UNDERLYING_ASA_ID: Final[ApplicationStateValue] = ApplicationStateValue(
        stack_type=TealType.uint64, static=True
    )

    # Smart ASA metadata
    TOTAL: Final[ApplicationStateValue] = ApplicationStateValue(
        stack_type=TealType.uint64
    )
    DECIMALS: Final[ApplicationStateValue] = ApplicationStateValue(
        stack_type=TealType.uint64, static=True
    )
    DEFAULT_FROZEN: Final[ApplicationStateValue] = ApplicationStateValue(
        stack_type=TealType.uint64
    )
    UNIT_NAME: Final[ApplicationStateValue] = ApplicationStateValue(
        stack_type=TealType.bytes
    )
    NAME: Final[ApplicationStateValue] = ApplicationStateValue(
        stack_type=TealType.bytes
    )
    URL: Final[ApplicationStateValue] = ApplicationStateValue(stack_type=TealType.bytes)
    METADATA_HASH: Final[ApplicationStateValue] = ApplicationStateValue(
        stack_type=TealType.bytes, static=True
    )
    MANAGER_ADDR: Final[ApplicationStateValue] = ApplicationStateValue(
        stack_type=TealType.bytes
    )
    RESERVE_ADDR: Final[ApplicationStateValue] = ApplicationStateValue(
        stack_type=TealType.bytes
    )
    FREEZE_ADDR: Final[ApplicationStateValue] = ApplicationStateValue(
        stack_type=TealType.bytes
    )
    CLAWBACK_ADDR: Final[ApplicationStateValue] = ApplicationStateValue(
        stack_type=TealType.bytes
    )
