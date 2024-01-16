# -*- coding: utf-8 -*-

from work_order_mediator import WorkOrderMediator
from order_manager import OrderManager
from file_manager import FileManager


def main():
    # Initialization of the main components of the program
    mediator = WorkOrderMediator()
    order_manager = OrderManager(mediator)
    file_manager = FileManager(mediator)

    # Loading orders from a file
    filename: str = "work_orders.txt"
    file_manager.load_orders_from_file(filename)

    # The main loop of the console interface
    while True:
        print("\nSelect an option:")
        print("[1] Add a new order")
        print("[2] Update order status")
        print("[3] Delete order")
        print("[4] Remove the team from the order")
        print("[5] Show all orders")
        print("[6] Finish")

        choice: str = input("> ")

        match choice:
            case '1':
                order_manager.input_and_create_order()
                file_manager.save_orders_to_file(filename)

            case '2':
                order_number: str = input("Enter the order number: ")
                brigade_specialization: str = input("Enter the specialization of the brigade: ")
                new_status: str = input("Is the work done? (yes/no): ").lower() in ["yes"]
                print(order_manager.update_order_status(order_number, brigade_specialization, new_status))
                file_manager.save_orders_to_file(filename)

            case '3':
                order_number: str = input("Enter the order number to delete: ")
                order_manager.remove_order(order_number)
                file_manager.save_orders_to_file(filename)

            case '4':
                order_number: str = input("Enter the order number: ")
                brigade_specialization: str = input("Enter the crew specialization to delete: ")
                order_manager.delete_brigade_from_order(order_number, brigade_specialization)
                print(f"Brigade {brigade_specialization} removed from the order {order_number}.")
                file_manager.save_orders_to_file(filename)

            case '5':
                order_manager.print_orders()

            case '6':
                break

if __name__ == "__main__":
    main()
