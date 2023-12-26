from game_data import data
from hol_ascii import logo, vs
from random import choice
from os import name, system


def get_random_person():
    return choice(data)


# def describe_random_person():
#     random_person = get_random_person()
#     print()
def ask_to_play():
    print(logo)
    first_person = get_random_person()
    print(
        f"Compare A: {first_person['name']} a, {first_person['description']} from {first_person['country']}"
    )
    print(vs)
    second_person = get_random_person()
    print(
        f"Against B: {second_person['name']} a, {first_person['description']} from {second_person['country']}"
    )


def display_results():
    ask_to_play()
    score = 0
    user_choice = input("Who has more followers? Type 'A' or 'B': ")
    stats = {"wins": 0, "losses": 0}
    if (
        user_choice == "A"
        and first_person["followers"] > second_person["followers"]
        or user_choice == "B"
        and second_person["followers"] > first_person["followers"]
    ):
        stats["wins"] += 1
    else:
        system("cls" if name == "nt" else "clear")
        print(logo)
        print(f"Sorry, that's wrong. Final Score: {stats}")
