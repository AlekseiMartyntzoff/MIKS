# -*- coding: utf-8 -*-

from typing import List, Tuple

from work_order import WorkOrder
from work_order_mediator import WorkOrderMediator


class OrderManager:
    """
    This class manages orders using WorkOrderMediator. 
    He is responsible for the logic associated with the article ordering,
    updating, deleting and outputting orders
    """

    # Initialization of the order manager with the broker
    def __init__(self, mediator: WorkOrderMediator) -> None:
        self.mediator: WorkOrderMediator = mediator

    # Create and add a new order
    def create_order(self, order_number: str, brigade_specialization: str, planned_start_date: str, completed: bool) -> None:
        self.mediator.add_order(order_number, brigade_specialization, planned_start_date, completed)

    # Update order status
    def update_order_status(self, order_number: str, brigade_specialization: str, new_status: bool) -> str:
        return self.mediator.update_order_status(order_number, brigade_specialization, new_status)

    # Deleting an order
    def delete_order(self, order_number: str) -> None:
        self.mediator.delete_order(order_number)

    # Removal of the team from the order
    def delete_brigade_from_order(self, order_number: str, brigade_specialization: str) -> None:
        self.mediator.delete_brigade_from_order(order_number, brigade_specialization)

    # Getting a list of all orders
    def get_orders(self) -> List[WorkOrder]:
        return self.mediator.get_orders()

    # Entering data and creating a new order
    def input_and_create_order(self) -> None:
        order_number: str = input("Enter the order number: ")
        specializations: Tuple[str] = ("plastering", "concrete works", "masonry", "electricity", "roofing", "plumbing", "landscape", "other")
        print("Select the specialization of the brigade:")
        for i, specialization in enumerate(specializations, 1):
            print(f"{i}. {specialization}")

        specialization_choice: int = int(input("Your choice (enter number): "))
        brigade_specialization = specializations[specialization_choice - 1]
        planned_start_date: str = input("Enter the planned start date of the works (YYYY-MM-DD format): ")
        completed: str = input("Is the work done? (yes/no): ").lower() in ["yes"]
        self.create_order(order_number, brigade_specialization, planned_start_date, completed)

    # Output of all orders
    def print_orders(self) -> None:
        for order in self.mediator.get_orders():
            print(order)

    # Deleting an order with a check for its existence
    def remove_order(self, order_number: str) -> None:
        orders_before: int = len(self.get_orders())
        self.delete_order(order_number)
        if len(self.get_orders()) < orders_before:
            print(f"Order {order_number} deleted")
        else:
            print("Order not found.")
