# Lines 1 - 3 is needed to get a filename from a user
from sys import argv

script, filename = argv

# open the file mentioned
txt = open(filename)

# print a message with the filename
print(f"Here's your file {filename}:")
# Take file and do the read command
print(txt.read())
# ask user to type filename again. 
print("Type the filename again:")
# take in users input but also display the greater sign symbol when asking
file_again = input("> ")
# open file again - default opens in read
txt_again = open(file_again)
# read and print the file.
print(txt_again.read())
