import sys

def sumOfSquares(number):
	sum = 0
	for n in number:
		sum = sum + int(n)* int(n)
	return sum

#test_cases = open(sys.argv[1], 'r')
test_cases = open('test.txt', 'r')
for test in test_cases:

	numbers = list(test)
	numbers = numbers[:-1]
	count = 0
	num = sumOfSquares(numbers)
	while ( num != 1 and count <= 100):
		numbers = list(str(num))
		num = sumOfSquares(numbers)
		count +=1
	if num == 1:
		print 1
	else:
		print 0
test_cases.close()
