from time import time

# 1. Use filter functions when it comes to insertion or deletion in a list
# primes = set((200, 386, 566, 735, 7))
# items = list(range(50))
# start_time = time()
# for prime in primes:rd)
#     items.remove(prime)
# # print(items)
# end_time = time()

# print(end_time - start_time)

# start_time = time()
# list_for_list = [number for number in items if number not in primes]
# end_time = time()
# print(end_time - start_time)

# start_time = time()
# new_list = list(filter(lambda number: number not in primes, items))
# end_time = time()
# print(end_time - start_time)


# map(2, filter(lambda number: number == 49, items))
# print(items)

items = list(range(300))
start_time = time()
print([2 if number == 277 else number for number in items])
end_time = time()
print(end_time - start_time)
start_time = time()
items[277] = 2
print(items)
end_time = time()
print(end_time - start_time)
