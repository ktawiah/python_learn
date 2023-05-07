import re

# Regex for password verification
strong_password_regex = (
    r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&#_\s])[A-Za-z\d@$!%*?&#_\s]{8,}$"
)
# Regex for email verification
email_regex = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
# Regex for url verification
url_regex = r"^(https?|ftp)://[^\s/$.?#].[^\s]*$"
# Regex for name verification
name_regex = (
    r"^(?!.*[A-Z]{2,}$)[a-zA-Z]{2,}(-|\s)[a-zA-Z]{1,}'?-?[a-zA-Z]{1,}\s?([a-zA-Z]{1,})?"
)

# name_list = [
#     "John Li",
#     "Emily-Gery Daniels Andy May Hamilton",
#     "Antwi",
#     "Mr. Watanabe",
#     "Watanabe",
#     "RoboCop Watanabe",
#     "Alice Watanabe",
#     "John Smith",
#     "John D'Largy",
#     "John Doe-Smith",
#     "John Doe Smith",
#     "Hector Sausage-Hausen",
#     "Mathias d'Arras",
#     "Martin Luther King",
#     "Ai Wong",
#     "Chao Chang",
#     "Alzbeta Bara",
#     "STEVE SMITH",
#     "Stev3 Smith",
#     "STeve Smith",
#     "Steve SMith",
#     "Steve Sm1th",
#     "d'Are to Beaware",
#     "Jo Blow",
#     "Hyoung Kyoung Wu",
#     "Mike O'Neal",
#     "Steve Johnson-Smith",
#     "Jozef-Schmozev Hiemdel",
#     "O'Henry Smith",
#     "Mathais d'Arras",
#     "Martin Luther King, Jr.",
#     "Downtown-James Brown",
#     "Darren McCarty",
#     "George De FunkMaster",
#     "Kurtis B-Ball Basketball",
#     "Ahmad el Jeffe",
# ]


# for name in name_list:
#     match = re.search(name_regex, name)
#     if match:
#         print(f"{name} is valid")
#     print(f"{name} is invalid")

# def is_strong_password():
#
#     password = input("Enter your password: ")
#     while not bool(re.match(strong_password_regex, password)):
#         password = input("Enter a strong password: ")
#     return f"{password} is a strong password"


# print(is_strong_password())
