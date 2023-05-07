"""Hangman Game."""
from random import choice


def hangman():
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

    STAGES = [
        """
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
""",
        """
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
""",
        """
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
""",
        """
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========""",
        """
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
""",
        """
  +---+
  |   |
  O   |
      |
      |
      |
=========
""",
        """
  +---+
  |   |
      |
      |
      |
      |
=========
""",
    ]
    print(LOGO)
    guessed_letter_function = lambda: input("Guess a letter: ")
    word_list = (
        "abruptly",
        "absurd",
        "abyss",
        "affix",
        "askew",
        "avenue",
        "awkward",
        "axiom",
        "azure",
        "bagpipes",
        "bandwagon",
        "banjo",
        "bayou",
        "beekeeper",
        "bikini",
        "blitz",
        "blizzard",
        "boggle",
        "bookworm",
        "boxcar",
        "boxful",
        "buckaroo",
        "buffalo",
        "buffoon",
        "buxom",
        "buzzard",
        "buzzing",
        "buzzwords",
        "caliph",
        "cobweb",
        "cockiness",
        "croquet",
        "crypt",
        "curacao",
        "cycle",
        "daiquiri",
        "dirndl",
        "disavow",
        "dizzying",
        "duplex",
        "dwarves",
        "embezzle",
        "equip",
        "espionage",
        "euouae",
        "exodus",
        "faking",
        "fishhook",
        "fixable",
        "fjord",
        "flapjack",
        "flopping",
        "fluffiness",
        "flyby",
        "foxglove",
        "frazzled",
        "frizzled",
        "fuchsia",
        "funny",
        "gabby",
        "galaxy",
        "galvanize",
        "gazebo",
        "giaour",
        "gizmo",
        "glowworm",
        "glyph",
        "gnarly",
        "gnostic",
        "gossip",
        "grogginess",
        "haiku",
        "haphazard",
        "hyphen",
        "iatrogenic",
        "icebox",
        "injury",
        "ivory",
        "ivy",
        "jackpot",
        "jaundice",
        "jawbreaker",
        "jaywalk",
        "jazziest",
        "jazzy",
        "jelly",
        "jigsaw",
        "jinx",
        "jiujitsu",
        "jockey",
        "jogging",
        "joking",
        "jovial",
        "joyful",
        "juicy",
        "jukebox",
        "jumbo",
        "kayak",
        "kazoo",
        "keyhole",
        "khaki",
        "kilobyte",
        "kiosk",
        "kitsch",
        "kiwifruit",
        "klutz",
        "knapsack",
        "larynx",
        "lengths",
        "lucky",
        "luxury",
        "lymph",
        "marquis",
        "matrix",
        "megahertz",
        "microwave",
        "mnemonic",
        "mystify",
        "naphtha",
        "nightclub",
        "nowadays",
        "numbskull",
        "nymph",
        "onyx",
        "ovary",
        "oxidize",
        "oxygen",
        "pajama",
        "peekaboo",
        "phlegm",
        "pixel",
        "pizazz",
        "pneumonia",
        "polka",
        "pshaw",
        "psyche",
        "puppy",
        "puzzling",
        "quartz",
        "queue",
        "quips",
        "quixotic",
        "quiz",
        "quizzes",
        "quorum",
        "razzmatazz",
        "rhubarb",
        "rhythm",
        "rickshaw",
        "schnapps",
        "scratch",
        "shiv",
        "snazzy",
        "sphinx",
        "spritz",
        "squawk",
        "staff",
        "strength",
        "strengths",
        "stretch",
        "stronghold",
        "stymied",
        "subway",
        "swivel",
        "syndrome",
        "thriftless",
        "thumbscrew",
        "topaz",
        "transcript",
        "transgress",
        "transplant",
        "triphthong",
        "twelfth",
        "twelfths",
        "unknown",
        "unworthy",
        "unzip",
        "uptown",
        "vaporize",
        "vixen",
        "vodka",
        "voodoo",
        "vortex",
        "voyeurism",
        "walkway",
        "waltz",
        "wave",
        "wavy",
        "waxy",
        "wellspring",
        "wheezy",
        "whiskey",
        "whizzing",
        "whomever",
        "wimpy",
        "witchcraft",
        "wizard",
        "woozy",
        "wristwatch",
        "wyvern",
        "xylophone",
        "yachtsman",
        "yippee",
        "yoked",
        "youthful",
        "yummy",
        "zephyr",
        "zigzag",
        "zigzagging",
        "zilch",
        "zipper",
        "zodiac",
        "zombie",
    )
    chosen_word = choice(word_list)
    display_guesses = list()
    life = 6
    print(chosen_word)

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
    hangman()
