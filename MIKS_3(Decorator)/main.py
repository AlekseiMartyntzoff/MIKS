# -*- coding: utf-8 -*-

from smart_home_server import SmartHomeServer
from logging_decorator import LoggingDecorator
from alert_decorator import AlertDecorator


# The main function is to demonstrate how a decorated server works
# Creates a server, wraps it in decorators and sends test messages
server = AlertDecorator(LoggingDecorator(SmartHomeServer()))

# Using a decorated server
server.handle_message("Simple message")
server.handle_message("House fire. Urgent attention needed!")
server.handle_message("Water leak. Urgent attention needed!")
