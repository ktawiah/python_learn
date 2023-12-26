if int(input("How many people are in your dinner group?")) >= 8:
    print("Then they would have to wait till tomorrow")
else:
    print("I will get your order ready then")

number = input("Give me a random number")
number = int(number)
if number % 10:
    print(str(number) + " is a multiple of 10")
else:
    print(str(number) + " is not a multiple of 10")

message = input(
    "Enter a series of pizza toppings of your preference. Enter quit if you want to stop."
)
while message != "quit":
    print("Wow! Nice choice. I love " + message.title() + " too.")
    break
