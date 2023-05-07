"""Pseudonym(fake name) generator"""
from random import choice


def generate_pseudonym():
    """Chooses random names two name tuples and print the combined name"""
    first_name_file = "Chapter_1 _Codes/Psuedonyms/first_names.txt"
    last_name_file = "Chapter_1 _Codes/Psuedonyms/last_names.txt"
    try:
        with open(first_name_file, "r", encoding="utf-8") as file_object:
            first_names = file_object.read().strip().split("\n")
    except FileNotFoundError:
        print(f"Sorry, the file {first_name_file} does not exist.")

    try:
        with open(last_name_file, "r", encoding="utf-8") as file_object:
            last_names = file_object.read().strip().split("\n")
    except FileNotFoundError:
        print(f"Sorry, the file {last_name_file} does not exist.")

    print("Welcome to the Psych 'Sidekick Name Picker.'\n")
    print("A name just like Sean would pick for Gus:\n\n")
    end_game = True
    while end_game:
        print(f"{choice(first_names)} {choice(last_names)}")
        end_game_response = input("Try again? (Press Enter else n to quit)\n")

        if end_game_response.lower() == "n":
            end_game = False


if __name__ == "__main__":
    generate_pseudonym()
