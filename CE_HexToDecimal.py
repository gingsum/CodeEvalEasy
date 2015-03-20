import sys

test_cases = open(sys.argv[1], 'r')
#test_cases = open("test.txt", 'r')
li = {'a':10, 'b':11, 'c':12, 'd':13, 'e':14, 'f':15}

for test in test_cases:
	test = test.strip()
	# store the digits in reverse order
	# first digit just mult by 1
	# second digit mult by 16^1
	# third digit mult by 16^2 and so on
	# use list for a to f
	test = test[::-1]
	nums = list(test)

	sum = 0
	for i in range(0,len(nums)):
		if test[i].isalpha():
			sum = sum + li[test[i]]*pow(16,i)
		else:
			sum = sum + int(test[i])*pow(16,i)
	print sum
