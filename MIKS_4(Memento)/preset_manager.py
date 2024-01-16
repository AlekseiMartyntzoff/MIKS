# -*- coding: utf-8 -*-

from typing import List

from memento import Memento
from equalizer_preset import EqualizerPreset


class PresetManager:
    """ 
    A class that manages the storage and restoration of preset states. 
    """

    def __init__(self) -> None:
        self._mementos: List[Memento] = []

    def save(self, preset: EqualizerPreset) -> None:
        # Saves the state of the preset.
        self._mementos.append(Memento(preset))

    def restore(self, preset: EqualizerPreset, index: int) -> None:
        # Restores the state of the preset. 
        memento = self._mementos[index]
        preset.__dict__ = memento.get_saved_state()

    def get_presets_count(self) -> int:
        # Returns the number of saved presets. 
        return len(self._mementos)
