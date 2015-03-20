# i is the number being checked
# n[i] is the number of i being checked
# n[i] is also the single count for i being checked
# each time you see n[i], increment that char by 1
# if that char and it's total count is equal to i 
#	and the corresponding count of n[i], than return true
# else return 0
# if all array return true, return 1

import sys
test_cases = open(sys.argv[1], 'r')

#test_cases = open('test.txt', 'r')

for test in test_cases:
	li = [0]*10
	test = test.strip()
	length = len(test)
	count = [0]*length
	match = True
	for i in range (0,length):
		li[int(test[i])] += 1  	# 0 1 2	= i = 
		count[i] = int(test[i])	# 1 2 3	= count[i] = li[i] 
	for i in range (0,length):
		if count[i] != li[i]:
			print 0
			match = False
			break
	if match:
		print 1

test_cases.close()