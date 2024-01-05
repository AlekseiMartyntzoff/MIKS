# -*- coding: utf-8 -*-

from typing import Dict, Type

from potion import Potion
from health_potion import HealthPotion
from strength_potion import StrengthPotion


class PotionFactory:
    """
    A factory class for creating potion objects.
    Implements the Flyweight pattern to reuse instances of potions
    """

    _potions: Dict[str, Potion] = {}

    @classmethod
    def get_potion(cls, potion_type: str) -> Potion:
        """
        Returns a potion instance. If an instance of the requested potion type
        doesn't exist it creates a new one and stores it in the _potions dictionary.
        """

        if not cls._potions.get(potion_type):
            if potion_type == "Health":
                cls._potions[potion_type] = HealthPotion()
            elif potion_type == "Strength":
                cls._potions[potion_type] = StrengthPotion()
        return cls._potions[potion_type]
