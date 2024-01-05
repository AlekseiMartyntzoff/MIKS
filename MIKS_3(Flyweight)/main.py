# -*- coding: utf-8 -*-

from typing import List

from character import Character
from potion_factory import PotionFactory
from potion import Potion


# Initialize characters
characters: List[Character] = [
    Character(name="Warrior", health=100, strength=75),
    Character(name="Mage", health=70, strength=25),
    Character(name="Archer", health=85, strength=60)
]

def main() -> None:
    """
    Main function to run the potion app
    Allows the user to choose a character and a potion then applies the potion and shows the effect on the character
    """

    print("Choose a character:")
    for i, character in enumerate(characters):
        print(f"{i + 1}. {character}")

    choice: int = int(input("Enter your choice (number): ")) - 1
    selected_character: Character = characters[choice]

    print("\nChoose a potion: \n1. Health Potion\n2. Strength Potion")
    potion_choice: int = int(input("Enter your choice (number): "))

    selected_potion: Potion
    if potion_choice == 1:
        selected_potion = PotionFactory.get_potion("Health")
    else:
        selected_potion = PotionFactory.get_potion("Strength")

    print("\nBefore applying potion:")
    print(selected_character)

    selected_potion.apply_effect(selected_character)

    print("\nAfter applying potion:")
    print(selected_character)

if __name__ == "__main__":
    main()
