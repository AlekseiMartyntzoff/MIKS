# -*- coding: utf-8 -*-

from equalizer_preset import EqualizerPreset


class Memento:
    """ 
    Memento class to save preset state. 
    """

    def __init__(self, preset: EqualizerPreset) -> None:
        self._state: dict = preset.__dict__.copy()

    def get_saved_state(self) -> dict:
        """ 
        Returns the saved state. 
        """

        return self._state
