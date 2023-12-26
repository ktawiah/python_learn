print("Welcome to the Love Calculator!")
name_1 = input("What is your name?\n")
name_2 = input("What is his/her name?\n")


def love_calculate(name_1, name_2):
    com_name = name_1.lower() + name_2.lower()
    true_count = 0
    love_count = 0
    score = ""
    for char in list("true"):
        true_count += com_name.count(char)

    for char in list("love"):
        love_count += com_name.count(char)

    score = str(true_count) + str(love_count)

    if int(score) < 10 or int(score) > 90:
        return f"Your score is {score}, you go together like coke and mentos."
    elif 40 <= int(score) <= 50:
        return f"Your score is {score}, you are alright together."
    else:
        return f"Your score is {score}."


if __name__ == "__main__":
    print(love_calculate(name_1, name_2))
