# -*- coding: utf-8 -*-

from abc import ABC, abstractmethod


class Manager(ABC):
    @abstractmethod
    def manage(self, question: str):
        pass
