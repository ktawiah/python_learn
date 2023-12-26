from time import time


def is_power_of_four(n: int) -> bool:
    """Determine if a number is a power of 4

    Parameters
    ----------
    n : int
        Number to validate

    Returns
    -------
    bool
        True or False based on whether power of 4 or not
    """

    if n <= 0:
        return False

    if n == 1:
        return True

    if n % 4 != 0:
        return False
    return is_power_of_four(n / 4)


def is_power_of_three(n: int) -> bool:
    if n <= 0:
        return False
    if n == 1:
        return True
    if n % 3 != 0:
        return False
    return is_power_of_three(n / 3)


if __name__ == "__main__":
    start_time = time()
    print(is_power_of_three(3000))
    end_time = time()
    print(end_time - start_time)
