# -*- coding: utf-8 -*-

from Manager import Manager


class CardManager(Manager):
    def manage(self, question: str) -> str:
        return f"Card Manager handles question: {question}"
