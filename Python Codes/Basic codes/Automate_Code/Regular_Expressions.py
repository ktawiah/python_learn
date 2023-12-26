import re

phone_number = re.compile(r"\d\d\d-\d\d\d-\d\d\d\d")

# Search() implemnetation
number = phone_number.search("My new number is 233-508-0718")
print(number.group())  # group() combines the matching pairs

# Adding parenthesis will create groups in the regex
phone_number = re.compile(r"(\d\d\d)-(\d\d\d-\d\d\d\d)")
number = phone_number.search("My new number is 233-508-0718")
print(number.group(1))
print(number.group(2))
print(number.group(0))
print(number.group())
# the finall() is also used ina a similar way

# Regex escape characters
"""\d   - Any numeric digit from 0 to 9.
\D   -Any character that is not a numeric digit from 0 to 9.
\w -  Any letter, numeric digit, or the underscore character.
(Think of this as matching “word” characters.)
\W -  Any character that is not a letter, numeric digit, or the
underscore character.
\s  -  Any space, tab, or newline character. (Think of this as
matching “space” characters.)
\S  -  Any character that is not a space, tab, or newline."""

vowelRegex = re.compile(r"\d+\s+\w")
vowelRegex.findall(
    "12 drummers",
    "11 pipers",
    "10 lords",
    "9 ladies",
    "8 maids",
    "7 swans",
    "6 geese",
    "5 rings",
    "4 birds",
    "3 hens",
    "2 doves",
    "1 partridge",
)

nameRegex = re.compile(r"^Franc")
nameRegex.search("Francois, Mike Whitney, Sagun Khatri")
print(nameRegex)

# [] - Character Set
# {} - Number of consecutive repetitions
# ^ - Begin Position
# $ - Ending

names = [
    "Fin Bindeabelle",
    "Geir Anders Berge",
    "HappyCodingRobot",
    "Ron Cromberge",
    "Sohil",
]
nameRegex = "^\w + \w+$"
for name in names:
    result = re.search(nameRegex, name)
    if result:
        print(name)
