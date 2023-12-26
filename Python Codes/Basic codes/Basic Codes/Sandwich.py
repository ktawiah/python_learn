items = []
prompt = input("How many items do you want in your sandwich?")
prompt = int(prompt)
print("Enter the items/n")
for value in range(0, prompt):
    item = input()
    items.append(item)


def sandwich_list(items_list):
    print("The sandwich you've ordered would contain: ")
    for item in items_list:
        print(item)


if "__main__" == __name__:
    sandwich_list([1, 34, 4])
