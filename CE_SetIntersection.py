import sys

#test_cases = open(sys.argv[1], 'r')
test_cases = open('test.txt', 'r')
for test in test_cases:
	list = test.split(";")
	list[-1] = list[-1].strip()
	firstHalf = list[0].split(",")
	secondHalf = list[1].split(",")

	current = ""
	for first in firstHalf:
		for second in secondHalf:
			if first == second:
				current = current + first + ","
	if current != "":
		print  current[:-1]
test_cases.close()
