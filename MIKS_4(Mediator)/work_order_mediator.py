# -*- coding: utf-8 -*-

from typing import List

from work_order import WorkOrder


class WorkOrderMediator:
    """
    The WorkOrderMediator class acts as a mediator, managing WorkOrder objects.
    It provides a centralized place to create update delete and retrieve order information.
    """

    def __init__(self) -> None:
        self.orders: List[WorkOrder] = []

    # Adding a new order
    def add_order(self, order_number: str, brigade_specialization: str, planned_start_date: str, completed: bool) -> None:
        order = WorkOrder(order_number, brigade_specialization, planned_start_date, completed)
        self.orders.append(order)

    # Updating the status of an existing order
    def update_order_status(self, order_number: str, brigade_specialization: str, new_status: bool) -> str:
        for order in self.orders:
            if order.order_number == order_number and order.brigade_specialization == brigade_specialization:
                order.completed = new_status
                return "Status updated"
        return "Order or crew not found"

    #Deleting an order by number
    def delete_order(self, order_number: str) -> None:
        self.orders = [order for order in self.orders if order.order_number != order_number]

    # Removal of the team from the order
    def delete_brigade_from_order(self, order_number: str, brigade_specialization: str) -> None:
        self.orders = [order for order in self.orders if not (order.order_number == order_number and order.brigade_specialization == brigade_specialization)]

    # Getting a list of all orders
    def get_orders(self) -> List[WorkOrder]:
        return self.orders
