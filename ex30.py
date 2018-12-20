# ex30 if else statements

# Set variables
people = 30
cars = 10
trucks = 15


# if cars is greater than people
if cars > people:
	print("We should take the cars.")
# else if cars is less than people print the following
elif cars < people:
	print("We should not take the cars.")
# and if no condition is met above do the following
else:
	print("We can't decide.")

# trucks is greater than cars print the following
if trucks > cars:
	print("That's too many trucks.")
# else if trucks is less than cars print the following
elif trucks < cars:
	print("Maybe we could take the trucks.")
# and if no condition is met than do the following
else:
	print("We still can't decide.")

# if people is greater than trucks do the following
if people > trucks:
	print("Alright, let's just take the trucks.")
# and if the above condition is not met do the following
else:
	print("Fine, let's stay home then.")


"""
1. The elif and else statement are being evaluated if the initial if condition is not met.
2. By changing different results are given

"""