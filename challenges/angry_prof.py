# angry professor
# a hackerrank algorithm challenge
# python version

# get number of test cases
test_cases = int(raw_input())
is_canceled = []
yes = 0
no = 0

# for each test case,
for i in range(0, test_cases):
	# get n integers (students), get k (cancelation threshold)
	students, required = raw_input().split()
	
	# get n arrival times
	arrivals = raw_input().split()

	for t in range(0, int(students)):
		time = int(arrivals[t])
		if time <= 0:
			no += 1
		elif time > 0:
			yes +=1

	if yes < int(required):
		is_canceled.append("YES")
	else:
		is_canceled.append("NO")

for c in range(0, len(is_canceled)):
	print is_canceled[c]











