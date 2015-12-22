# chapter 5 exercises
# from Think Python

# exercise 5.3
	# write a function named check_fermat that takes 4 args: a, b, c, n that
	# checks to see if Fermat's theorem holds.

def check_fermat(list):
	a = list[0]
	b = list[1]
	c = list[2]
	n = list[3]

	print (a*n) + (b*n)
	print c*n

	if n > 2:
		print "Holy smokes, Fermat was wrong!"
	else:
		print "No, that doesn't work."

print "Give me 4 space-separated numbers: "
numbers = raw_input("> ").split()
int_nums = []

# convert input to int
for i in range(len(numbers)):
	convert_to_int = int(numbers[i])
	int_nums.append(convert_to_int)

check_fermat(int_nums)


# exercise 5.4
	# write a function that takes 3 int args and that prints yes or no if
	# you can form a triangle, otherwise, you can.

def is_triangle(sides):
	"""takes an integer list, checks for the largest value then
	prints something if you can form a triangle, else otherwise.
	"""

	a = sides[0]
	b = sides[1]
	c = sides[2]

	if a > b:
		large_num = a
	else:
		large_num = b

	if large_num > c:
		largest = large_num
	else:
		largest= c

	if 


print "Give me 3 numbers: "
side = raw_input("> ").split()
sides = []

for i in range(len(side)):
	if i < 3:
		side_int = int(side[i])
		sides.append(side_int)
	else:
		break

is_triangle(sides)

























