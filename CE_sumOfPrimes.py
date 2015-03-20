import math

sum = 2+3
index = 3
i = 4
while True:
	prime = True
	for j in range(2, int(math.sqrt(i))+1) :
		if i%j == 0:
			prime = False
			break
	if prime == True:
		sum += i
		index+=1
	if index == 1001:
		break
	i+=1
print sum