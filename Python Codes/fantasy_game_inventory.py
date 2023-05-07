"""Generates inventory information"""


def display_inventory():
    """Takes input of items from the user, loops through them and returns details of inventory"""
    inventory = {}
    done_inputting = False
    while not done_inputting:
        key = input("Enter item name: ")
        value = int(input("Enter item number: "))
        inventory[key] = value

        other_inventory = input(
            "Are there other inventory? Enter 'Yes' to enter more or 'No'"
        )
        if other_inventory.casefold() == "Yes":
            done_inputting = False
        done_inputting = True

    for key, value in inventory.items():
        print(f"Inventory: \n{str(value)} {key}")

    total_inventory = 0
    for value in inventory.values():
        total_inventory += value

    return f"Total number of items: {total_inventory}"


if __name__ == "__main__":
    print(display_inventory())
