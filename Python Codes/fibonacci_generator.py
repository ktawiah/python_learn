"""Fibonacci Sequence Generator"""
import functools


@functools.lru_cache(maxsize=1000)
def fibonacci(number):
    """Returns the fibonacci sequence up to the number, n inputted by the user"""
    if not isinstance(number, int):
        raise TypeError("n must be a positive int")
    if number < 1:
        raise ValueError("n must be a positive integer")
    if number == 1:
        return 1
    if number == 2:
        return 1
    if number > 2:
        return fibonacci(number - 1) + fibonacci(number - 2)


if __name__ == "__main__":
    for num in range(1, 9):
        print(fibonacci(num), end=" ")
