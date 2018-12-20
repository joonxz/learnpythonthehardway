# prepare to take arguments
from sys import argv
# disperse arguments to variables
script, filename = argv
# Tell user about what is going to happen to the file
print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")
# wait for user input with a question mark
input("?")
# open the file and set it to write
print("Opening the file...")
target = open(filename, 'w')
# Truncate or erase the contents of the file
print("Truncating the file. Goodbye!")
target.truncate()
# ask user for input to write in the file
print("Now I'm going to ask you for three lines.")
# take input from user and store it in variables
line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("Now I'm going to write these to the file.")
# write each line in file 
target.write(line1)
target.write("/n")
target.write(line2)
target.write("/n")
target.write(line3)
target.write("/n")
# close the file after it has been used
print("And finally, we close it.")
target.close()
