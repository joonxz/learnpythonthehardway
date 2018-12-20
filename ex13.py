# In console I would be able to input arguments when I run the program
from sys import argv
# read the WYSS section for how to run this
# Arguments will be expanded to these variables. 
script, first, second, third = argv

# Print each variable with the value
print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)