from time import time
from string import ascii_lowercase
from palingram_spell import load_word_list

word_list = set(load_word_list())
start_time = time()
list_collection = set(filter(lambda x: x in list(ascii_lowercase), word_list))
print(list_collection)
end_time = time()
print(end_time - start_time)

start_time = time()
ascii_collection = []
for word in word_list:
    if word.lower() in list(ascii_lowercase):
        ascii_collection.append(word)
print(ascii_collection)
end_time = time()
print(end_time - start_time)

start_time = time()
ascii_words = [word for word in word_list if word.lower() in list(ascii_lowercase)]
print(ascii_words)
end_time = time()
print(end_time - start_time)
