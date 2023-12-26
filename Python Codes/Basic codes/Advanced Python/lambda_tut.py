from math import sqrt

str_list = ["Kel", "Angel", "May", "King"]
lamb_list = [1, 2, 3, 4, 5, 6]
print(list(map(lambda x: sqrt(x), lamb_list)))
print(list(filter(lambda x: x % 2 == 0, lamb_list)))  # All even numbers in list
print(list(map(lambda x: x[0], filter(lambda x: x[0] == "A", str_list))))
print(list(filter(lambda x: x[0] == "K", str_list)))
print(list(map(lambda x: pow(x, 2), filter(lambda x: x % 2 != 0, lamb_list))))
books = [
    {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "price": 9.99},
    {"title": "To Kill a Mockingbird", "author": "Harper Lee", "price": 7.99},
    {"title": "The Catcher in the Rye", "author": "J.D. Salinger", "price": 6.99},
    {"title": "Pride and Prejudice", "author": "Jane Austen", "price": 5.99},
    {"title": "1984", "author": "George Orwell", "price": 8.99},
]
# Code used to filter the title of a book based on the name of the author and price of the book
print(
    list(
        map(
            lambda book: book["title"],
            filter(
                lambda book: book["author"] == "Jane Austen" and book["price"] == 5.99,
                books,
            ),
        )
    )
)

people = [
    {"name": "Alice", "age": 25, "profession": "teacher"},
    {"name": "Bob", "age": 30, "profession": "doctor"},
    {"name": "Charlie", "age": 20, "profession": "engineer"},
    {"name": "Dave", "age": 35, "profession": "teacher"},
    {"name": "Eve", "age": 28, "profession": "engineer"},
]


# Returns the name of the people whose ages are less than 30
print(
    list(
        map(
            lambda person: person["name"],
            filter(lambda person: person["age"] < 30, people),
        )
    )
)


def lead_me(amount: str, data: int) -> bool:
    return amount


lead_me(data="kevin", amount=1)
