"""Finds Palindromes and Palingrams from a dictionary word list."""


def load_word_list():
    """Loads the words in dictionary into a list."""
    file_path = "Chapter_2_codes/Palingram/word-list.txt"
    try:
        with open(file_path, "r", encoding="utf-8") as word_list_file:
            content = word_list_file.read().strip().split("\n")
    except FileNotFoundError:
        print(f"Sorry {file_path} doesn't exist.")
    return content


def find_palindromes():
    """Returns a list of palindromic words"""
    word_list = set(load_word_list())
    palindrome_list = []
    for word in word_list:
        if word == word[::-1]:
            palindrome_list.append(word)

    return palindrome_list


def find_palingrams():
    """Finds dictionary palingrams."""
    palingram_list = []
    word_list = set(load_word_list())
    for word in word_list:
        end = len(word)
        rev_word = word[::-1]
        if end > 1:
            for i in range(end):
                if word[i:] == rev_word[: end - i] and rev_word[end - i :] in word_list:
                    palingram_list.append((word, rev_word[end - i :]))
                if word[:i] == rev_word[end - i :] and rev_word[: end - i] in word_list:
                    palingram_list.append((rev_word[: end - i], word))
    return palingram_list


if __name__ == "__main__":
    print(find_palindromes())
    print(find_palingrams())
