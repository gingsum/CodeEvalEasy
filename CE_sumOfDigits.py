import sys

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
  	n = list(test)
  	sum = 0
  	for num in n:
  		if num.isdigit():
  			sum += int(num)
  	print sum
test_cases.close()