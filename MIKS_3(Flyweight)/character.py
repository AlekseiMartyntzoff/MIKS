# -*- coding: utf-8 -*-

class Character:
    """
    Represents a character in the game
    Each character has a name, health, and strength attribute
        name (str): The name of the character
        health (int): The health points of the character
        strength (int): The strength points of the character
    """

    def __init__(self, name: str, health: int, strength: int):
        self.name: str = name
        self.health: int = health
        self.strength: int = strength

    def __str__(self) -> str:
        return f"{self.name}: Health = {self.health}, Strength = {self.strength}"
