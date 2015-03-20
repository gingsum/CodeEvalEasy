import sys

def printOut(numA,numB,numC):
	a = int(numA)
	b = int(numB)
	c = int(numC)
	for index in range(1,c):
		if index%a == 0 and index%b == 0:
			print "FB",
		elif index%a == 0:
			print "F",
		elif index%b == 0:
			print "B",
		else:
			print index,
	if c%a == 0 and c%b == 0:
		print "FB",
	elif c%a == 0:
		print "F",
	elif c%b == 0:
		print "B",
	else:
		print c,
	print ""

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
  	n = test.split()
 	printOut(n[0],n[1],n[2])

