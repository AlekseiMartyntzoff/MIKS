# -*- coding: utf-8 -*-

from potion import Potion
from character import Character


class StrengthPotion(Potion):
    """
    A potion that increases the character's strength.
    Inherits from the Potion class and implements the apply_effect method
    """

    def apply_effect(self, character: Character) -> None:
        character.strength += 5  # Increase character's strength by 5
