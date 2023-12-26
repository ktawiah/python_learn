import re

pattern = r"Bat(wo)?man|Figma"
str_name = "My name is Batwoman and I love to use Figma"

name = re.search(pattern, str_name)
print(name.group())
# Page 185
# Question 20
num_regex = r".+,\d{3}$"
num_list = ["42", "1,234", "6,368,745"]

for num in num_list:
    match = re.search(num_regex, num)
    if match:
        print(num)

# Question 21
name_list = [
    "Haruto Watanabe",
    "haruto Watanabe",
    "Mr. Watanabe",
    "Watanabe",
    "RoboCop Watanabe",
    "Alice Watanabe",
]
name_regex = r"^[A-Z][a-zA-Z]+\sWatanabe"
for name in name_list:
    match = re.search(name_regex, name)
    if match:
        print(name)

sentence_regex = re.compile(
    "^(Alice|Bob|Carol)\s(eats|pets|throws)\s(basballs|cats|apples)", re.I
)
sentences = [
    "Alice eats apples.",
    "ALICE THROWS FOOTBALLS.",
    "Bob pets cats.",
    "BOB EATS CATS.",
    "RoboCop eats apples.",
    "Carol throws baseballs.",
]
for sentence in sentences:
    match = re.search(sentence_regex, sentence)
    if match:
        print(sentence)
