# -*- coding: utf-8 -*-

from CardManager import CardManager
from DepositManager import DepositManager
from LoanManager import LoanManager
from ManagerType import ManagerType


question: str = input("Question: ")

manager = None

for manager_type in ManagerType:
    if manager_type.value in question:
        if manager_type == ManagerType.CARD:
            manager = CardManager()
        elif manager_type == ManagerType.DEPOSIT:
            manager = DepositManager()
        elif manager_type == ManagerType.LOAN:
            manager = LoanManager()
        break

if manager:
    response: str = manager.manage(question)
    print(response)
else:
    print("No manager available for this question. Sorry!")
