"""Rock, Paper, Scissors Game"""
import random


def rock_paper_scissors():
    paper = """
        _______
    ---'   ____)__
            ______)
            _______)
            _______)
    ---.__________)
    """
    scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
    """
    rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
    """

    choice = [rock, paper, scissors]
    user_choice = input(
        "What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n"
    )
    computer_choice = random.choice(choice)
    print(choice[int(user_choice)])

    print(f"Computer chose:\n{computer_choice}")

    if choice[int(user_choice)] == computer_choice:
        print("You won!")
    else:
        print("You lost! Play again?")


rock_paper_scissors()
