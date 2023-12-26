"""Rock, Paper, Scissors Game"""
from random import choice
from rps_logo import get_paper, get_rock, get_scissors


def play_rock_paper_scissors():
    scissors = get_scissors()
    rock = get_rock()
    paper = get_paper()

    rps_choices = [rock, paper, scissors]

    while True:
        user_selection = input(
            "What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n"
        )
        while int(user_selection) not in [0, 1, 2]:
            user_selection = input("Enter a number between 0 - 2(both inclusive): ")

        user_choice = rps_choices[int(user_selection)]
        computer_choice = choice(rps_choices)
        print(f"You chose:\n {user_choice}")

        print(f"Computer chose:\n{computer_choice}")
        if user_choice == rps_choices[0] and computer_choice == rps_choices[2]:
            print("You won!!!")
        elif user_choice == rps_choices[1] and computer_choice == rps_choices[0]:
            print("You won!!!")
        elif user_choice == rps_choices[2] and computer_choice == rps_choices[1]:
            print("You won!!!")
        elif user_choice == computer_choice:
            print("Draw game!!!")
        else:
            print("You lost!!!")
        end_game_response = input("Wanna play again? Yes/No.")
        while end_game_response not in ["Yes", "No"]:
            end_game_response = input("Wrong input. Check case or enter valid input: ")

        if end_game_response == "No":
            break


if __name__ == "__main__":
    play_rock_paper_scissors()
