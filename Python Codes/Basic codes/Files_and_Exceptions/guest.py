""" Add and Prints out the details of the user to and from txt file"""

from pyinputplus import inputInt, inputEmail, inputURL, inputDate
from validator_collection import email

FILE_PATH = "Basic codes/Files_and_Exceptions/guest.txt"


def validate_data() -> dict:
    """Collects user input for validation

    Returns
    -------
    dict
        Dictionary containing data
    """
    newDate = inputDate(prompt="Enter date here: ", formats=[])
    url = inputURL("Enter url of user: ")
    integer = inputInt("Enter integer: ")
    py_email = inputEmail("Enter email: ")
    user_email = email("kelvin@gmail.com")

    return {"url": url, "integer": integer, "email": py_email}


def get_details():
    """Retrieves user's name, age, and date of birth

    Returns
    -------
    dict
        Dictionary containing user data
    """

    uname = input("Enter user's name: ")
    age = int(input("What's your age:"))
    dob = input("What's your date of birth(mmddyyyy)")

    return {"username": uname, "user_age": age, "user_dob": dob}


def write_to_file():
    """Writes user data to txt file"""
    user_data = get_details()
    with open(FILE_PATH, "w", encoding="UTF-8") as file_object:
        file_object.write("The details of the user are as follows")
        file_object.write(f"The user's name is {user_data['username']}")
        file_object.write(f"The age of the user is {user_data['user_age']}")
        file_object.write(f"The date of birth of the user is {user_data['user_dob']}")


def print_user_details():
    """Outputs details of user in txt file"""
    with open(FILE_PATH, "r", encoding="UTF-8") as file_object:
        print(file_object.read())


def collect_data(amount: int) -> dict:
    """Collects the user data for querying api

    Parameters
    ----------
    amount : int
        Amount of humans in population specified

    Returns
    -------
    str
        The analyses graph name and population output
    """

    return amount + 2


if __name__ == "__main__":
    validate_data()
    # write_to_file()
    # print_user_details()


# class GuestUser:
#     """Describes the user object"""

#     def __init__(self, username, user_age, user_dob):
#         """Initializes guest user object

#         Args:
#             username (str): Name of user
#             user_age (str): Age of user
#             user_dob (str): Date of birth of user
#         """
#         self.username = username
#         self.user_age = user_age
#         self.user_dob = user_dob

#     def input_details

#     # def inputfile(self):
#     #     file_path = "/home/kelly/Documents/Python Projects/Basic codes/Files_and_Exceptions/guest.txt"
#     #     with open(file_path, "w", encoding="UTF-8") as file_object:
#     #         file_object.write(
#     #             "\nThe details of the user are as follows\nThe name of the user is "
#     #             + self.username
#     #             + "\n"
#     #         )
#     #         file_object.write("This user is aged " + str(self.age) + "\n")
#     #         file_object.write(
#     #             "The user's date of birth is "
#     #             + self.dob[:2]
#     #             + " / "
#     #             + self.dob[2:4]
#     #             + " / "
#     #             + self.dob[4:8]
#     #             + "\n"
#     #         )

#     #     with open(file_path, "r") as file_object:
#     #         print(file_object.read())
