# -*- coding: utf-8 -*-

from abc import ABC, abstractmethod

from character import Character


class Potion(ABC):
    """
    Abstract base class for all potion types
    Defines the interface for applying effects to characters
    """

    @abstractmethod
    def apply_effect(self, character: Character) -> None:
        pass
