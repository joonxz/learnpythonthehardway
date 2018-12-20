# Start program with an input which is a name
from sys import argv
# Seperate arguments into variables
script, user_name = argv
# a string that would be included when prompted
prompt = '> '
# Introduce user
print(f"Hi {user_name}, I'm the {script} script.")
print("I'd like to ask you a few questions.")
# Ask a question
print(f"Do you like me {user_name}?")
# Store answer in variable
likes = input(prompt)
# ask another question
print(f"Where fo you live {user_name}?")
# store answer in variable
lives = input(prompt)

# ask another question
print("What kind of computer do you have?")
# store answer in variable
computer = input(prompt)


# print values with a statement. Kind of fun.
print(f"""
	Alright, so you said {likes} about liking me.
	You live in {lives}. Not sure where that is.
	And you have a {computer}. Nice.
	""")