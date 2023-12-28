# -*- coding: utf-8 -*-

import datetime

from smart_home_server import SmartHomeServer


class LoggingDecorator:
    '''
    A decorator to add message logging functionality
    This class wraps any SmartHomeServer compatible object and adds logging of all messages to a file
    '''

    def __init__(self, wrapped: SmartHomeServer) -> None:
        self.wrapped = wrapped

    def handle_message(self, message: str) -> None:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_message = f"{timestamp}: {message}"
        print(f"Logging message: {log_message}")
        with open("log.txt", "a") as log_file:
            log_file.write(log_message + "\n")
        self.wrapped.handle_message(message)
