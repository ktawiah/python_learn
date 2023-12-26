"""Blind Auction Game"""
from blind_auction_ascii_art import logo
import os


def get_name():
    name = input("What is your name: ")
    return name


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def get_bid():
    while True:
        bid = input("What is your bid: $")
        if bid.isdigit():
            return int(bid)
        print("Invalid input. Enter a valid number: $")


def play_game():
    print(logo)
    print("Welcome to the secret auction program")
    bids_so_far = {}
    while True:
        player_name = get_name()
        player_bid = get_bid()
        bids_so_far[player_name] = player_bid
        end_bidding = input("Are there any other bidders? Type 'yes' or 'no'.\n")
        while end_bidding not in ["yes".casefold(), "no".casefold()]:
            print("Wrong input. Enter either 'yes' or 'no'\n")

        if end_bidding == "no".casefold():
            break
        else:
            clear_screen()
    for key, value in bids_so_far.items():
        if value == max(bids_so_far.values()):
            return f"The winner is {key} with a bid of ${value}"


if __name__ == "__main__":
    print(play_game())
