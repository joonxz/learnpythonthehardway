# This program is going to calculate the c in the pythagorean theorem

def pythFindC(a, b):

	a = a ** 2
	b = b ** 2
	c = (a + b)**(1/2.0)

	# Round the number
	c = round(c, 2)

	print "Result of C is ", c

pythFindC(3,4)
pythFindC(7,9)
pythFindC(2,3)
pythFindC(10,12)