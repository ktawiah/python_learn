from validator_collection import checkers


def get_email():
    email = input("Enter your email address here: ")
    while not checkers.is_email(email):
        email = input("Enter a correct email address: ")
    print(f"Your email address is {email}")


if __name__ == "__main__":
    get_email()
