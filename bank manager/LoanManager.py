# -*- coding: utf-8 -*-

from Manager import Manager


class LoanManager(Manager):
    def manage(self, question: str) -> str:
        return f"Loan Manager handles question: {question}"
