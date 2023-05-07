def number_of_cans_needed():
    get_width = lambda: input("Enter the width: ")
    get_height = lambda: input("Enter the height: ")
    get_coverage = lambda: input(
        "Enter the coverage per square meter on the paint can: "
    )
    wall_width = int(get_width())
    wall_height = int(get_height())
    wall_coverage = int(get_coverage())

    return f"You'll need {round((wall_height*wall_width) / wall_coverage)}"


if __name__ == "__main__":
    print(number_of_cans_needed())
