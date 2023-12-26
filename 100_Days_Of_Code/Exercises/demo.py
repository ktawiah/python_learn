import math
import random

list_1 = [1, 3, 4, 8]
for x in iter(list_1):
    print(x, end="")

for index, name in enumerate(list_1):
    print(name, end="")

list_2 = [3, 4, 6]
for i, j in zip(list_1, list_2):
    print(i, j)

print((5.4))
print(math.ceil(5.4))
print(math.pow(7, 4))
print(math.pi)
print(round(math.pi, 7))
print(random.randrange(15, 29))

name = "0.5"
if name.isdecimal:
    print("My name is me")


def printPicnic(itemsDict, leftWidth, rightWidth):
    print("PICNIC ITEMS".center(leftWidth + rightWidth, "-"))
    for k, v in itemsDict.items():
        print(k.ljust(leftWidth, ".") + str(v).rjust(rightWidth))


picnicItems = {"sandwiches": 4, "apples": 12, "cups": 4, "cookies": 8000}
printPicnic(picnicItems, 12, 5)
printPicnic(picnicItems, 20, 6)

print(name.rjust(20, "_"))
print(name.ljust(10, "*"))


