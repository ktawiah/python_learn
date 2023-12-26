for number in range(100, 999):
    if number == sum(list(map(lambda x: int(x) ** 3, list(str(number))))):
        print(number)
