"""Pig latin word converter."""


def generate_pig_latin_form():
    """Returns the pig latin form of an input"""
    consonant_list = tuple("bcdfghjklmnpqrstvwxyz".upper())

    word_to_change = input("Enter word to change to pig latin form: ")
    if word_to_change[0] in consonant_list:
        return print(f"{word_to_change}ay")
    return f"{word_to_change}yay"


if __name__ == "__main__":
    print(generate_pig_latin_form())
