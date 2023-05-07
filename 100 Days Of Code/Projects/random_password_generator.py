"""
    Generates random password from specified constraints
      like the number of letters, numbers, and special characters
"""
from string import ascii_lowercase
import random

letters = list(ascii_lowercase)
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

print("Welcome to PyPassword Generator!")
letter_num = int(input("How many letters would you like in your password?\n"))
symbols_num = int(input("How many symbol would you like\n"))
numbers_num = int(input("How many numbers would you like?\n"))

num_str = ""
symbol_str = ""
letter_str = ""
for num in range(numbers_num):
    num_str += random.choice(numbers)

for letter in range(letter_num):
    letter_str += random.choice(letters)

for symbol in range(symbols_num):
    symbol_str += random.choice(symbols)

pass_list = list(f"{letter_str}{num_str}{symbol_str}")

random.shuffle(pass_list)
rand_pass = "".join(pass_list)
print(rand_pass)
