import math

for i in range(1000, 1, -1):
	prime = True
	for j in range(int(math.sqrt(i)),2,-1):
		if i%j == 0:
			prime = False
			break
	
	if prime == True:
		numS = str(i)
		numRS = str(i)[::-1]
		if numS == numRS:
			print numRS
			break
