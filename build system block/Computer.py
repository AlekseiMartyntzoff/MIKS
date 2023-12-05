# -*- coding: utf-8 -*-

class Computer:
    def __init__(self):
        self._motherboard: str = ""
        self._processor: str = ""
        self._memory: str = ""
        self._storage: str = ""
        self._graphics_card: str = ""
        self._sound_card: str = ""
        self._dvd_drive: str = ""

    def __str__(self):
        return str(self.__dict__)
