pizza_price = 0
pepperoni_price = 0
extra_cheese = 0
print("Welcome to the Python Pizza Deliveries!")
pizza_size = input("What size pizza do you want? S, M, or L ")
while True:
	if pizza_size == "S":
		pizza_price = 15
	elif pizza_size == "M":
		pizza_price = 20
	else:
		pizza_price = 25
		
	if input("Do you want pepperoni? Y or N ") == "Y":
		if pizza_size == "S":
			pepperoni_price = 2
		else:
			pepperoni_price = 3
			
	if input("Do you want extra cheese? Y or N ") == "Y":
		extra_cheese = 1
		
	print(f"Your final bill is: {pizza_price + pepperoni_price + extra_cheese}")
	break
