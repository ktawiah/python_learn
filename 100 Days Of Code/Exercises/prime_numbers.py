def is_prime():
    get_number = lambda: input("Enter number to number to check if it's a prime: ")
    number_to_check = int(get_number())
    for num in range(2, number_to_check):
        if number_to_check % num == 0:
            return False
    return True


if "__main__" == __name__:
    print(is_prime())
