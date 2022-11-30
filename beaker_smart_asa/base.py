"""
This file implements the base class from which all Smart ASA components should inherit.
"""


from beaker import Application


class BaseSmartASA(Application):
    """Abstract class for all components of this project"""

    def __init__(self):
        """Fixing TEAL version as suggested by PyTeal/Beaker"""
        super().__init__(version=6)
