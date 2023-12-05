# -*- coding: utf-8 -*-

from Manager import Manager


class DepositManager(Manager):
    def manage(self, question: str) -> str:
        return f"Deposit Manager handles question: {question}"
