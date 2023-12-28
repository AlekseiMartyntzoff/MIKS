# -*- coding: utf-8 -*-


class SmartHomeServer:
    '''
    The basic server class for a smart home system
    In theory responsible for processing messages from client modules 
    (in our case it displays a message on the screen)
    '''

    def handle_message(self, message: str) -> None:
        print(f"Final handling of message: {message}" + "\n")
