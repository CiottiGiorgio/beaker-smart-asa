"""
This file implements the main skeleton of Smart ASA.
"""

from beaker_smart_asa.smart_asa_manager import SmartASAManager
from beaker_smart_asa.smart_asa_user import SmartASAUser


class SmartASA(SmartASAManager, SmartASAUser):
    """This class implements the SmartASA contract (not yet) compliant with ARC-0020"""
