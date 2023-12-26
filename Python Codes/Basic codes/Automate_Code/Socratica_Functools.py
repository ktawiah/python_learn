# import random

# # name = "Kelvin Tawiah"
# # vowels = "aeiou"
# # for char in iter(name):
# #     if char.casefold() in vowels:
# #         print(char, end=" ")

# # random_float = random.random()
# # print(random_float * 5)

# sides = ["Heads", "Tails"]
# choice = input()
# random_side = random.choice(sides)
# print(random_side)
name = "Kelvin"
name_list = [1, 3, 2, 4]


def tut_func():
    name.upper()
    name_list.reverse()
    print(name)
    print(name_list)


tut_func()
print(name)
print(name_list)

print(list(map(lambda x: x + 3, name_list)))


# def add_7(x):
#     return x + 7


def is_Odd(x):
    return x % 2 != 0


print(list(map(lambda x: x + 7, name_list)))
print(list(map(lambda x: x % 2 != 0, name_list)))
