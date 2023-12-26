from math import pi

person = {"name": "Jenn", "age": 23}

print(f"My name is {person['name']} and I am {person['age']} years old.")

for s in (f"The value is {n}" for n in range(1, 11)):
    print(s)

print(f"The value of pi to the power 4 is {pi:.4f}")

a = dict(A=1, B=2)
print(a["A"])

print(list(zip("hello", range(6))))
new_dict = dict(zip("Kelvin", range(6)))
print(new_dict)

b = {"Jane Does": 5, "Mary Allen": 6}
print(b)

my_array = [2, 4, 5, 6]
print(type(my_array))
