from time import time


def is_prime(n: int) -> bool:
    mid_value = n // 2
    if mid_value == 1:
        return True
    while mid_value >= 2:
        if n % mid_value == 0:
            return True
        mid_value -= 1
    return False


print(is_prime(9))
