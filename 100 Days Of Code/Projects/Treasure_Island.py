"""Treasure Island Game"""
import re


def treasure_island():
    """A simple treasure Island game. Takes input for the direction of game until treasure is found"""
    print(f"Welcome to Treasure Island.\nYour mission is to find the treasure.\n")
    direction = input(
        'You\'re at a cross road. Where do you want to go? Type "left" or "right"\n'
    )

    if direction.casefold() == "right":
        print("You fell into a hole.\n Game over.")
    elif direction.casefold() == "left":
        print("Do you want to swim or wait?\n")
        swim = input()
        if swim.casefold() == "swim":
            print("Game over")
        elif swim.casefold() == "wait":
            print(
                "You are almost there!!!\n Choose one door. Type 'blue', 'red' or 'yellow'\n"
            )
            door = input()
            if door.casefold() == "red" or door.casefold() == "blue":
                print("Game over!")
            elif door.casefold() == "yellow":
                print("Hurray!!! You reached the treasure box. Congratulations.")


treasure_island()
