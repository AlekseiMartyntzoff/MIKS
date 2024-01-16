# -*- coding: utf-8 -*-

from typing import List


class EqualizerPreset:
    """ 
    A class that represents an equalizer preset
    """

    def __init__(self, name: str, genre: str, bands: List[int]) -> None:
        self.name: str = name
        self.genre: str = genre
        self.bands: List[int] = bands  # List of 12 offset values

    def set_preset(self, bands: List[int]) -> None:
        # Installing new preset settings
        self.bands: List[int] = bands

    def __str__(self) -> str:
        return f"Equalizer Preset [Name: {self.name}, Genre: {self.genre}, Bands: {self.bands}]"
