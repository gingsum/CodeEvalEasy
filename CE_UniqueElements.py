import sys

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
	list = test.split(",")
	list[-1] = list[-1].strip()
	current = list[0]
	for i in range(0,len(list)):
		if current != list[i]:
			sys.stdout.write(current+",")
			current = list[i]
	print current
test_cases.close()
