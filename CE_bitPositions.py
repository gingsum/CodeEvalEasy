import sys

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
  	n = test.split(",")
  	binary = list(bin(int(n[0]))[::-1])  	
  	if binary[int(n[1])-1] == binary[int(n[2])-1]:
  		print "true"
  	else:
		print "false"

test_cases.close()