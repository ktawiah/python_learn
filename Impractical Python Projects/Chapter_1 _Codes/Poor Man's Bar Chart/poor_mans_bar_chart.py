"""Poor Man's Bar Chat"""


def bar_chart():
    """Returns a bar char for all the characters that occur in a sentence input"""
    sentence = input("Enter your sentence here\n").lower()
    chart_dictionary = {}
    for character in sentence:
        chart_dictionary[character] = []

    for character in sentence:
        if character in chart_dictionary.keys():
            chart_dictionary[character].append(character)

    return chart_dictionary


if __name__ == "__main__":
    print(bar_chart())
