import sys
import string

test_cases = open(sys.argv[1],'r')
#test_cases = open("test.txt",'r')

a = list(string.ascii_lowercase)
dic = {a[i]: 0 for i in range(0,26)}
li = range(26,0,-1)

for test in test_cases:
	test = test.strip()
	letters = list(test)

	unique = []
	count = []

	for char in letters:
		if char.lower().isalpha():
			current_char = char.lower()
			exist = False
			for i in unique:
				if i == current_char:
					exist = True
			if exist:
				for j in range(0,len(unique)):
					if unique[j] == current_char:
						count[j] += 1
			else:
				unique.append(current_char)
				count.append(1)
	count = sorted(count)[::-1]
	sum = 0
	for k in range(0,len(count)):
		sum = sum + count[k]*li[k]
	print sum
