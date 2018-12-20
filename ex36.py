# Ex 36 - My own program ..... still deciding...

"""
My hunger cannot be satisfied until i find my mothers 
special food. Until then I scour the streets to find food that 
may temporarily satisfy me. Unfortunately, since 
nothing else satisfies me enough I may die of hunger.

Objective: Find your mother's food. 
As time goes, a health counter keeps going down.
You will encounter opportunities to eat and events 
that will effect your health. 
Some foods will may make your health go down some foods
can stop the counter for a few moments. Ultimately,
you have to get to your mothers food.

Need:
Health Counter
Foods
- empanada. Hold for a few seconds.
- rice and beans with chicken. Finally home
- chicken salad. Doesn't do anything
- fast foods - hot dogs, tacos with picante. DOWN

Time
- health and time go hand in hand.
- 

Events - what type of events?
- parade...prolongs foot traffic
- dog chase
- police investigation
- 

notes:
Mom's food is across the other side of town.
Events happen as the counter goes down. 


"""

from sys import exit

def win():
	print("yummmmmmmmmm")

def die(reason):
	print(" Your", reason, " made you freeze in place and die of hunger. Good Job!")

def divider():
	print("===========================================")

def healthCounter(health):
	#health = health + currHealth
	print("My health is", health)

def third(debuff):
	# health and debuff = health
	divider()
	print(" You keep walking and notice that you are almost there.")
	print(" As I walk, I noticed my good neighbor struggling with her groceries.")
	print(" She notices me and asks if I can help")
	print(" Should I help? yes or no")
	choice = input("> ")

	if choice == "yes":
		print(" Oh, Thank you says \"Dona Juana\".")
		print(" As I was reach her home to drop her groceries Dona Juana says")
		print(" Your mom gave some food to give you to you. She said you must be hungry.")
		print(" My eyes lit up...")
		win()
	elif choice == "no":
		print(" I ignore her and run to my house. I feel like I am going to pass out.")
		print(" When I get home, I don't smell food...but I see a note. It reads...")
		print(" \"My son, I had to leave early. The neighbor has the food I made you. Bye mom\"")
		die(" lack of being a good samaritan")
	else:
		die(" indecision")

def second(debuff):
	divider()
	print(" Let's keep it moving...")
	print(" As you are walking, you notice someone pick poketing a tourist!")
	print(" The tourist noticed but wasn't fast enough to catch the thief.")
	print(" You apparently are a few feet away. What are we going to do? ")
	print(" Are you going to help? yes or no")
	choice = input("> ")

	if choice == "yes":
		divider()
		print(" I stick the foot out, as the thief runs frantically away, he trips and falls on the pavement!")
		print(" You grab the stolen item and return it to the tourist.")
		print(" Merci! Merci! says the tourist as she lays a huge kiss the cheek.")
		third(0)
	elif choice == "no":
		divider()
		print(" I don't care I am hungry. That's not my problem.")
		print(" The thief almost gets away, another samaritan stops the thief.")
		print(" The good samaritan gets angry at you for not stopping and punches you.")
		print(" Lose 50 health and now you have a blackeye!")
		third(-50)
	else:
		divider()
		print(" Since you can't decide.")
		die("indecision")


def first(counterDebuff):
	# counter starts with the debuff
	# counter is going down as the game goes along.
	# It goes down every second
	divider()
	healthCounter(counterDebuff)

	print(" On our way!....Who is that approaching?")
	print(" Someone is asking for directions. What do you do?")
	print(" Give directions?")
	choice = input("> ")
	if choice == "yes":
		print(" Awwww thanks. As they hand you a Snickers bar.")
		print(" +5 Points to health")
		second(5)
	else:
		print(" I ducked and dodge but I heard a rumble in my stomach.")
		print(" I looked down, tripped and hit the pavement.")
		print(" Minus 10 Health")
		second(-10)


def countStart(user):
	health = 100
	healthCounter(health)

	print("Start walking?")
	choice = input("> ")
	if choice == "yes":
		print("Awesome!", user, "don't let my hunger get to 0!")
		first(0)
	else:
		print("Oh come on, I'm hungry")
		# Start counter at 90
		first(-10)

def start():
	print(" Work was gruesome, didn't have lunch. Meetings all day")
	print("\"I need to get home, hmmmm mom's food!\", Francis says")
	print("\"I will perish if I dont get home soon \"")
	print("What's your name, player?")
	name = input("> ")
	print("Take me home", name, "before I perish!")

	countStart(name)

# Initiate program
start()
