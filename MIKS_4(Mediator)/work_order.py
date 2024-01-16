# -*- coding: utf-8 -*-


class WorkOrder:
    """
    The WorkOrder class represents a specific order in the system. 
    It contains all the necessary information about the order such as the order number
    the specialization of the crew the planned start date of the work and the status of completion.
    """

    # Initialize order with basic details
    def __init__(self, order_number: str, brigade_specialization: str, planned_start_date: str, completed: bool) -> None:
        self.order_number: str = order_number
        self.brigade_specialization: str = brigade_specialization
        self.planned_start_date: str = planned_start_date
        self.completed: bool = completed

    # Representation of the order object as a string
    def __str__(self) -> str:
        status = 'Done' if self.completed else 'Not done'
        return f"{self.order_number},{self.brigade_specialization},{self.planned_start_date},{status}"
