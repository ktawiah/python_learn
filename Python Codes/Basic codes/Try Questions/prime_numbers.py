"""Program used to validate prime numbers"""

import math
from pyinputplus import inputInt, inputYesNo
from pathlib import Path


def get_primes() -> list:
    """Collects primes numbers for validation
    Returns:
    -------
    list: List of primes numbers
    """

    prime_list = []
    number_of_primes = inputInt(
        prompt="Enter number of primes to validate\n", default=1, min=1
    )

    for number in range(number_of_primes):
        if number == 0:
            prime_number = inputInt("Enter first prime number: ")
        else:
            prime_number = inputInt("Enter next prime number: ")

        prime_list.append(prime_number)

    return prime_list


def validate_prime() -> str:
    """Loops through list of prime numbers and outputs result
    Returns:
    ------
    str: Output saying number is prime or not
    """

    prime_list = get_primes()
    print(prime_list)

    for number in prime_list:
        if number <= 1:
            print(f"{number} is not a prime")
            continue

        is_prime = True
        for divisor in range(2, math.isqrt(number) + 1):
            if number % divisor == 0:
                print(f"{number} is not a prime")
                is_prime = False
                break

        if is_prime:
            print(f"{number} is a prime")


def keep_idiot_busy() -> str:
    """A program which repeatedly asks the same question and requires 'no' to quit

    Returns
    -------
    str
        _description_
    """

    while True:
        response = inputYesNo(prompt="Want to know how to keep an idiot busy?\n ")
        if response.casefold() == "no":
            print("Thank you. Have a nice day!")
            break


def learn_paths():
    """Learn pathlib module"""

    path = Path("Basic codes/")
    print(path.exists())


if __name__ == "__main__":
    # print(validate_prime())
    # print(keep_idiot_busy())
    learn_paths()


# num = int(input('Enter number: '))

# class PrimeNumber:
#     def __init__(self, number: int):
#         self.number = number

#     def find_if_prime(self):
#         is_prime = True
#         for digit in range(2, self.number):
#             if self.number % digit == 0:
#                 is_prime = False
#                 break

#         if is_prime:
#             print(f'{self.number} is a prime number')
#         else:
#             print(f'{self.number} is not a prime number')

# PrimeNumber(num).find_if_prime()
