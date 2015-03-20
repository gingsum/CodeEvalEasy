import sys

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
  	n = test.split()
 	for word in reversed(n):
 		print word,
 	print ""
test_cases.close()