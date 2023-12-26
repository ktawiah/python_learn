fav_number = {"ken": 5, "Ben": 6, "Dan": 8, "Gad": 3}
for key, value in sorted(fav_number.items()):
    print(key.title() + "'s favorite number is " + str(value))

for key, value in sorted(fav_number.items()):
    print(f"{key.title()}'s favorite number is {value}")

Rivers = {"nile": "Egypt", "Pra": "Ghana", "Felicia": "US"}
for key, value in Rivers.items():
    print(key.title() + " runs through " + value.title())

fav_languages = {"Andy": "Python", "Lord": "Ruby", "Dickson": "Java", "Raf": "C#"}
for key, value in fav_languages.items():
    print(f"{key.title()}'s favorite programming language is {value.title()}")

fav_langs = {"King": ["Python", "Ruby", "Go"], "Lex": ["Django", "C#", "Java"]}
for key, value in fav_langs.items():
    print(str(key.title()) + "'s favorite programming languages are ")
    print(value)

pets = {
    "jaguar": {"kind": "cat", "owner": "King"},
    "dog": {"kind": "domestic", "owner": "OG"},
}
for key, value in pets.items():
    print(
        "There are so many pets in stock. The "
        + key.title()
        + " is a "
        + value["kind"]
        + " and it is owned by "
        + value["owner"]
    )
