# represents the amount of cars
cars = 100
# each car seats 4
space_in_a_car = 4
# There are 30 drivers
drivers = 30
# And 90 passengers
passengers = 90
# With only so many drivers there will be a lot of cars not driven
cars_not_driven = cars - drivers
# drivers and cars become the same since each driver will take a car
cars_driven = drivers
# ideally each driver takes people in their car. 
carpool_capacity = cars_driven * space_in_a_car
# Average # of passengers in each car
average_passengers_per_car = passengers / cars_driven

print "There are", cars, "cars available."
print "There are only", drivers, "drivers available"
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today"
print "We need to put about", average_passengers_per_car, "in each car"


# car_pool_capacity is not defined means that the variable was never defined previously.
# If 4.0 changes to 4. The variable is not a floating #, it becomes an integer
