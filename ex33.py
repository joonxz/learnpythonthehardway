# EX 33


numbers = []


def printNumbers(number, increment):
	i = 0
	incrementBy = increment
	
	while i < number:
		print(f"At the top i is {i}")
		numbers.append(i)


		i = i + incrementBy
		print("Numbers now: ", numbers)
		print(f"At the bottom i is {i}")
	
	"""
	for i in range(number):
		print(f"At the top of i is {i}")
		numbers.append(i)

		print("Numbers now: ", numbers)
		print(f"At the top of i is {i}")
	"""

print("The numbers: ")

for num in numbers:
	print(num)

# printNumbers(10)
printNumbers(12, 4)


"""
1. Convert this while-loop to a function that you can call, 
and replace 6 in the test (i < 6) with a variable.

2. Use this function to rewrite the script to try 
different numbers.

3. Add another variable to the function arguments that you 
can pass in that lets you change the + 1 on line 8 
so you can change how much it increments by.

4. Rewrite the script again to use this function to see 
what effect that has.

5. Write it to use for-loops and range. Do you need 
the incrementor in the middle anymore? What happens if you 
do not get rid of it?
I do not need the incrementor anymore if i write it as a for loop
since the for loop automatically increments by 1. 

"""