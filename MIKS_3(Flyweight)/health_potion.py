# -*- coding: utf-8 -*-

from potion import Potion
from character import Character


class HealthPotion(Potion):
    """
    A potion that increases the character's healt
    Inherits from the Potion class and implements the apply_effect method.
    """

    def apply_effect(self, character: Character) -> None:
        character.health += 10  # Increase character's health by 10
