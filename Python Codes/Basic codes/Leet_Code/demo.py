list_1 = {1, 2, 3}
list_2 = {3, 5, 6}

for i, num in zip(list_1, list_2):
    print(i, num)

name = "Paname"
print(list(zip(name, range(8))))
new_dict = dict(zip(list_1, list_2))
print(new_dict)
