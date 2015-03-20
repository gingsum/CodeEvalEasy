import sys

#test_cases = open(sys.argv[1], 'r')
test_cases = open('test.txt', 'r')
for test in test_cases:
	list = test.split(",")
	list[-1] = list[-1].strip()
	current = list[0]
	exist = False
	#print len(current),
	for i in range(len(current)-1, -1, -1):
		if list[1] == current[i]:
			print i+1
			exist = True
			break
	if exist == False:
		print -1
	
test_cases.close()
