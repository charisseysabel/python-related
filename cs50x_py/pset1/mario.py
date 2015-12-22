# pset1: mario
# from CS50x
# Build a half pyramid according to user's height input
# python version

height = int(raw_input("> Give me a number between 0 and 23: "))
if height < 0 or height > 23:
	print "Invalid input."

for row in range(1, height + 1):
	print ((" " * (height - 1)) + ("#" * row)) * 2
	height -= 1