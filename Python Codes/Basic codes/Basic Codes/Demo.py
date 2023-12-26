L1 = [1, 2, 3]
L2 = [2, 3, 4]
L3 = []

for x, y in zip(L1, L2):
    L3.append(x * y)
print(L3)
print(__name__)
