from re import fullmatch
from ascii_arts import logo
from os import system, name

print(logo)


def add(first_number, second_number):
    return float(first_number) + float(second_number)


def subtract(first_number, second_number):
    return float(first_number) - float(second_number)


def divide(first_number, second_number):
    return float(first_number) / float(second_number)


def multiply(first_number, second_number):
    return float(first_number) * float(second_number)


def get_first_number():
    first_number = input("Enter the first number: ")
    while not fullmatch("[0-9.]+", first_number):
        first_number = input("Enter a valid input: ")
    return first_number


def get_second_number():
    second_number = input("Enter the second number: ")
    while not fullmatch("[0-9.]+", second_number):
        second_number = input("Enter a valid input: ")
    return second_number


def calculate(first_number=get_first_number()):
    while True:
        operators = {
            "+": add,
            "-": subtract,
            "*": multiply,
            "/": divide,
        }

        for operator in operators:
            print(operator)

        user_operator_input = input("Pick an operator: ")
        while not fullmatch("[-+/*]+", user_operator_input):
            user_operator_input = input("Enter a valid operator: ")

        second_number = get_second_number()
        result = operators[user_operator_input](first_number, second_number)
        print(f"{first_number} {user_operator_input} {second_number} = {result}")
        response = input(
            f"Type 'y' to continue with {result}, type 'n' to start a new calcualation, or type 'q' to quit: "
        )

        if response == "y":
            calculate(first_number=result)

        if response == "n":
            system("cls" if name == "nt" else "clear")
            calculate(first_number=get_first_number())

        if response == "q":
            return


if __name__ == "__main__":
    print(calculate())
