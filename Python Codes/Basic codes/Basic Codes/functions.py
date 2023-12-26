""" This module elaborates the blah blah blah """
size = input("What is the size of shirt you would like? S/M/L/XL")
message = input("What message should be printed on the shirt")


def make_shirt(shirt_size: str, shirt_message: str) -> str:
    """_summary_

    Args:
        shirt_size (str): _description_
        shirt_message (str): _description_

    Returns:
        str: _description_
    """
    print(
        "You've ordered a shirt of size "
        + shirt_size
        + "and the message "
        + shirt_message
        + " would be printed on it"
    )


make_shirt(size, message)

models = []
number = input("How many models would you like to enter?: ")
number = int(number)
for num in range(0, number):
    model = input("Enter model name: ")
    models.append(model)


def print_model(model_list):
    """Prints all modules specified by user

    Args:
        model_list (list): string
    """
    for value in model_list:
        print("Printing model: " + value)


print_model(models)
