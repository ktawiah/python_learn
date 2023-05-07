import cProfile
from palingram_spell import find_palindromes, find_palingrams
from time import time

cProfile.run("find_palindromes()")
cProfile.run("find_palingrams()")

start_time = time()
find_palindromes()
find_palingrams()
end_time = time()
print(end_time - start_time)
