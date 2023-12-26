""" Practice from Socratica on regex """

import re

names = [
    "Fin Bindeabelle",
    "Geir Anders Berge",
    "HappyCodingRobot",
    "Ron Cromberge",
    "Sohil",
    "m!sha",
]
NAME_REGEX = r"^\w+ \w+$"
BEGIN_C = r"C\w*"
GET_LAST = r"[a-zA-Z!]+$"
for name in names:
    result = re.search(GET_LAST, name)
    if result:
        print(name)
        print(result.start())  # Part of string where a match started
        print(result.end())
