import sys

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
  	n = test.split(",")
  	index = 0
 	while True:
 		if int(n[0]) <= index*int(n[1]):
 			break
 		index+=1
 	print index*int(n[1])
test_cases.close()