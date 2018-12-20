# Ex 29 What if statements

people = 20
cats = 30
dogs = 15


if people < cats:
	print("Too many cats! The world is doomed!")


if people > cats:
	print("Not many cats! The world is saved!")


if people < dogs:
	print("The world is drooled on!")

if people > dogs:
	print("The world is dry!")


dogs += 5

if people >= dogs:
	print("People are greater than or equal to dogs.")

if people <= dogs:
	print("People are less than or equal to dogs.")

if people == dogs:
	print("People are dogs.")


""" 
1. The if first gets evaluated than if the condition is 
met the code within it is executed
2. python expects an indentation within the if. Its the way that the 
compiler knows that it is the code that gets evaluated if condition is met
3. If it is not indent, it will throw an error that it an indent is missing
4. Yes, you can put other boolean expressions in the if statement
5. If you change the values, the results will change
"""
