# -*- coding: utf-8 -*-

from logging_decorator import LoggingDecorator


class AlertDecorator:
    '''
    A decorator for adding functionality to send alerts 
    When the "alert" keyword is detected in a message the class simulates sending an email alert.
    ''' 
    
    def __init__(self, wrapped: LoggingDecorator) -> None:
        self.wrapped = wrapped

    def send_email(self, message: str, alert_type: str) -> None:
        # Imitation of sending an email
        print(f"Alert: {alert_type} | Sending email for: {message}")

    def handle_message(self, message: str) -> None:
        if 'House fire' in message:
            self.send_email(message, "House fire")
        elif 'Water leak' in message:
            self.send_email(message, "Water leak")
        self.wrapped.handle_message(message)
