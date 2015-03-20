import sys
#test_cases = open(sys.argv[1], 'r')
test_cases = open('test.txt', 'r')
for test in test_cases:
	test = test.strip()
	length = len(test)
	count = [0]*length
	for i in range (0,length):
		count[i] = int(test[i])
		
test_cases.close()