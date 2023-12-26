nums = []
number = input('Enter the number of elements in the list: ')
output = []
number = int(number)
for value in range(0, number):
    integer = input('Enter number: ')
    integer = int(integer)
    nums.insert(value, integer)

prompt = input('Enter target: ')
target = int(prompt)

for x in range(0, number-1):
    if nums[x] + nums[x + 1] == target:
        output.append(x)
        output.append(x + 1)
        print(output)
    else:
        x += 1
