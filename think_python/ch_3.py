# Think Python
# chapter 3 exercises

# exercise 3.3
	# write a function named right_justify that takes a string named s as param and
	# prints the string with enough leading spaces so that the last letter
	# of the string is in column 70 of the display
def right_justify(s):
	str_len = 70 - len(s)
	print " " * str_len  + s
	
s = raw_input()
right_justify(s)


# exercise 3.4
def do_twice(f, v):
	f(v)
	f(v)

def print_spam(s):
	print s

def do_four(f, v):
	do_twice(f, v)
	do_twice(f, v)

s = raw_input()
do_four(print_spam, s)


# exercise 3.5
	# print a box

plus = "+"
dash = "-"
pipe = "|"
space = " "

corners = plus + (dash * 4) + plus + (dash * 4) + plus
side = pipe + (space * 4) + pipe + (space * 4) + pipe

print corners
print side
print side
print side
print side
print corners
















