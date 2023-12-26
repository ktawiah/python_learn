from os import system, name
from random import choice

cards = (11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10)


def get_player_cards():
    user_cards = []
    for i in range(2):
        user_cards.append(choice(cards))
    return user_cards


def get_computer_cards():
    computer_cards = []
    for i in range(2):
        computer_cards.append(choice(cards))
    return computer_cards


def hit():
    user_cards = get_player_cards()
    user_cards.append(choice(range(1, 10)))
    return user_cards


# def stand():
#     return
def ask_to_play_game():
    play_game_response = input(
        "Do you want to play a game of Blackjack? Type 'yes' or 'no': "
    )
    while play_game_response not in ["yes", "no"]:
        play_game_response = input("Enter a valid response: ")
    # if play_game_response == "no":
    #     return

    if play_game_response == "yes":
        system("cls" if name == "nt" else "clear")
        play_game()


def play_game():
    user_cards = get_player_cards()
    computer_cards = get_computer_cards()
    print(f"Your cards: {user_cards}")
    print(f"Computer's first card: {computer_cards[0]}")

    reqest_response = input("Type 'y' to get another card, type 'n' to pass: ")
    while reqest_response not in ["y", "n"]:
        reqest_response = input("Enter a valid response: ")

    if reqest_response == "n":
        if sum(user_cards) > sum(computer_cards) and sum(user_cards) < 21:
            print(f"Your final hand: {user_cards}")
            print(f"Computer's final hand {computer_cards}")
            print("You win")
        elif sum(new_user_cards) == sum(computer_cards):
            print(f"Your final hand: {new_user_cards}")
            print(f"Computer's final hand {computer_cards}")
            print("Draw")
        else:
            print(f"Your final hand: {user_cards}")
            print(f"Computer's final hand {computer_cards}")
            print("You lose")

    if reqest_response == "y":
        new_user_cards = hit()
        if sum(new_user_cards) > sum(computer_cards) and sum(new_user_cards) < 21:
            print(f"Your final hand: {new_user_cards}")
            print(f"Computer's final hand {computer_cards}")
            print("You win")
        elif sum(new_user_cards) == sum(computer_cards):
            print(f"Your final hand: {new_user_cards}")
            print(f"Computer's final hand {computer_cards}")
            print("Draw")
        else:
            print(f"Your final hand: {new_user_cards}")
            print(f"Computer's fiinal hand {computer_cards}")
            print("You lose")

    ask_to_play_game()


if __name__ == "__main__":
    ask_to_play_game()
    play_game()
