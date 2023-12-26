#Page 154
def printTable():
    tableData = [
        ['apples', 'oranges', 'cherries', 'banana'],
        ['Alice', 'Bob', 'Carol', 'David'],
        ['dogs', 'cats', 'moose', 'goose']
    ]

    for i in range(0, len(tableData)):
        fruits, owners, animals = tableData[0], tableData[1], tableData[2]

    for fruit, owner, animal in zip(fruits, owners, animals):
        print(f'{fruit} {owner} {animal}')

    print(f'\n')
    
    for i in range(0, 4):
        print(f'{fruits[i]} {owners[i]} {animals[i]}')

print(printTable())