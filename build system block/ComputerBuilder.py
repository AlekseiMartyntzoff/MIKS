# -*- coding: utf-8 -*-

from Computer import Computer

class ComputerBuilder:
    def __init__(self):
        self._computer = Computer()

    @property
    def motherboard(self):
        return self._computer._motherboard

    @motherboard.setter
    def motherboard(self, value):
        self._computer._motherboard = value

    @property
    def processor(self):
        return self._computer._processor

    @processor.setter
    def processor(self, value):
        self._computer._processor = value

    @property
    def memory(self):
        return self._computer._memory

    @memory.setter
    def memory(self, value):
        self._computer._memory = value

    @property
    def storage(self):
        return self._computer._storage

    @storage.setter
    def storage(self, value):
        self._computer._storage = value

    @property
    def graphics_card(self):
        return self._computer._graphics_card

    @graphics_card.setter
    def graphics_card(self, value):
        self._computer._graphics_card = value

    @property
    def sound_card(self):
        return self._computer._sound_card

    @sound_card.setter
    def sound_card(self, value):
        self._computer._sound_card = value

    @property
    def dvd_drive(self):
        return self._computer._dvd_drive

    @dvd_drive.setter
    def dvd_drive(self, value):
        self._computer._dvd_drive = value

    def build(self):
        return self._computer
