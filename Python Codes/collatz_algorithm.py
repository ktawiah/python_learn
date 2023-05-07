""" 
Collatz Algorithm always gives you 1 after sucessive divisions
and multiplication
"""


def get_number():
    """Returns number for collatzs"""
    number = int(input("Enter the number for the collatz game: "))
    while number <= 0:
        number = int(input("Enter number > 0: "))
    return number


def run_collatz():
    """Generates the collatz sequence"""
    try:
        number = get_number()
        while number != 1:
            if number % 2 == 0:
                print(number / 2)
                number = number / 2
            else:
                print(number * 3 + 1)
                number = number * 3 + 1
    except ZeroDivisionError():
        print("Error: Argument invalid")


if __name__ == "__main__":
    run_collatz()
