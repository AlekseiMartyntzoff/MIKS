# -*- coding: utf-8 -*-

from work_order_mediator import WorkOrderMediator
from work_order import WorkOrder


class FileManager:
    """
    This class is responsible for working with files
    in particular for reading and saving order data
    It uses WorkOrderMediator to access order data
    """

    # Initialize file manager with broker
    def __init__(self, mediator: WorkOrderMediator) -> None:
        self.mediator: WorkOrderMediator = mediator

    # Saving orders to a txt file
    def save_orders_to_file(self, filename: str) -> None:
        with open(filename, 'w') as file:
            for order in self.mediator.get_orders():
                file.write(str(order) + '\n')

    # Loading orders from a txt file
    def load_orders_from_file(self, filename: str) -> None:
        try:
            with open(filename, 'r') as file:
                for line in file:
                    parts = line.strip().split(",")
                    if len(parts) == 4:
                        order_number, brigade_specialization, planned_start_date, completed_str = [part.strip() for part in parts]
                        completed: bool = completed_str == 'Done'
                        self.mediator.add_order(order_number, brigade_specialization, planned_start_date, completed)
        except FileNotFoundError:
            # The file was not found at the beginning of work, a new one will be created during further work
            print(f"File {filename} not found. A new file will be created.")
