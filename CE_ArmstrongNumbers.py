import sys

test_cases = open(sys.argv[1], 'r')
#test_cases = open("test.txt",'r')

for test in test_cases:
	test = test.strip()
	nums = list(test)
	power = len(nums)

	sum = 0
	for n in nums:
		sum = sum + pow(int(n),power)

	if sum == int(test):
		print "True"
	else:
		print "False"