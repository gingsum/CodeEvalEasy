import sys

test_cases = open(sys.argv[1], 'r')
#test_cases = open("test.txt", 'r')

for test in test_cases:
	test = test.strip()
	numbers = test.split(',')
	current_number = int(numbers[0])
	mod_number = int(numbers[1])
	while current_number >= mod_number:
		current_number = current_number - mod_number
	print current_number
