from ascii_arts import logo

print(logo)


def get_first_number():
    number = input("What's is the first number?: ")
    while not number.isdigit():
        number = input("Input should be a number. Enter a valid input.")
    return float(number)


def get_next_number():
    number = input("What's is the next number?: ")
    while not number.isdigit():
        number = input("Input should be a number. Enter a valid input.")
    return float(number)


def get_operator():
    operator_list = ("+", "/", "-", "*")
    for operator in operator_list:
        print(operator)
    operator = input("Pick an operator: ")
    while operator not in operator_list:
        operator = input("Enter a valid operator: ")
    return operator


def calculate(first_number=get_first_number()):
    operator_chosen = get_operator()
    next_number = get_next_number()
    if operator_chosen == "+":
        result = first_number + next_number
    elif operator_chosen == "-":
        result = first_number - next_number
    elif operator_chosen == "/":
        result = first_number / next_number
    else:
        result = first_number * next_number
    print(f"{first_number}{operator_chosen}{next_number} = {result}")
    return result


def continue_calculation():
    calculate()
    while True:
        choice = input(
            "Type 'y' to continue with 2.5, type 'n' to start a new calcualation, or type 'q' to quit: "
        )
        while choice not in ["y", "n", "q"]:
            choice = input("Input should either be 'y' or 'n'. Enter a valid input: ")

        if choice == "y":
            calculate(first_number=calculate())
        elif choice == "n":
            calculate(first_number=get_first_number())
        else:
            break


if __name__ == "__main__":
    print(continue_calculation())
