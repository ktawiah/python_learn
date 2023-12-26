"""Hangman Game."""
from random import choice
from stages import get_stages


def load_word_list():
    file_path = "100_Days_Of_Code/Projects/Hangman/word_list.txt"
    try:
        with open(file_path, "r", encoding="utf-8") as file_object:
            word_list = file_object.read().strip().split("\n")
    except FileNotFoundError:
        print(f"Sorry {file_path} does not exist.")
    return word_list


def play_hangman():
    """Returns life state based of guess."""
    LOGO = """ 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    """

    STAGES = get_stages()

    print(LOGO)
    guessed_letter_function = lambda: input("Guess a letter: ")
    word_list = load_word_list()

    chosen_word = choice(word_list)
    display_guesses = list()
    life = 6
    # print(chosen_word)

    for i in range(len(chosen_word)):
        display_guesses.append("_")

    while True:
        guessed_letter = guessed_letter_function().lower()
        if guessed_letter in display_guesses:
            print(f"You've already entered {guessed_letter}. Try again.")
        if guessed_letter in chosen_word:
            for index, letter in enumerate(chosen_word):
                if letter == guessed_letter:
                    display_guesses[index] = guessed_letter
            print(" ".join(display_guesses))
        else:
            print(
                f"You guessed {guessed_letter}, that's not in the word, You lose a life\n",
                STAGES[life],
            )
            life -= 1

        if "_" not in display_guesses:
            print("You win!!")
            break

        if life < 0:
            print("You lose...Try again?")
            break


if __name__ == "__main__":
    play_hangman()
