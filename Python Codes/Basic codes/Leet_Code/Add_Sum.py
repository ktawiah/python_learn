from llist import sllist

l1 = sllist([2, 4, 3])
l2 = sllist([5, 6, 4])

# reverse the order of the nodes in l1 in-place
l1.append(6)
print(l1)
# iterate over the reversed list using a for loop
for item in l1:
    print(item)

# create a new list that contains the elements of l2 in reverse order using a list comprehension
reversed_list = sllist([item for item in reversed(l2)])

print(reversed_list)
print(reversed_list[2])


