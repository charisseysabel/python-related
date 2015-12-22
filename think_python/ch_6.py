# chapter 6 exercises
# think python

# using incremental development

# exercise 6.1
# calculate the distance between 2 points
# distance = ((x2 - x1)^ + (y2 - y1)^2)^2

import math

def distance(x1, y1, x2, y2):
	dx = x2 - x1
	dy = y2 - y1
	dsquared = dx**2 + dy**2
	result = math.sqrt(dsquared)
	print result
	return result

distance(1, 2, 4, 6)

# exercise 6.2
# write a function called hypotenuse that returns the length of the hypotenuse 
# of a right triangle given the lengths of 2 legs as args

def hypotenuse(a, b):
	squared = (a**2) + (b**2)
	result = math.sqrt(squared)
	print result

hypotenuse(5, 12)

# exercise 6.3
# write a function that returns true if x <= y <= z
# or false otherwise

def is_between(x, y, z):
	if x <= y and y <= z:
		print "true"
		return True
	else:
		print "false"
		return False

is_between(1, 2, 3)
