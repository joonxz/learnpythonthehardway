# represents the amount of cars
c = 100
# each car seats 4
s = 4
# There are 30 drivers
d = 30
# And 90 passengers
p = 90
# With only so many drivers there will be a lot of cars not driven
n = c - d
# drivers and cars become the same since each driver will take a car
a = d
# ideally each driver takes people in their car. 
cp = a * s
# Average # of passengers in each car
ap = p / a

print "There are", c, "cars available."
print "There are only", d, "drivers available"
print "There will be", n, "empty cars today."
print "We can transport", cp, "people today."
print "We have", p, "to carpool today"
print "We need to put about", ap, "in each car"


# car_pool_capacity is not defined means that the variable was never defined previously.
# If 4.0 changes to 4. The variable is not a floating #, it becomes an integer
