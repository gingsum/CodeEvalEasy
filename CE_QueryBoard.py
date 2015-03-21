import sys

#test_cases = open(sys.argv[1],'r')
test_cases = open("test.txt",'r')

SET_SPACE = 256
matrix = [[0]*SET_SPACE for i in range(SET_SPACE)]

def setCol(a,b):
	for i in range(0,SET_SPACE):
		matrix[i][a] = b
def setRow(a,b):
	for j in range(0,SET_SPACE):
		matrix[a][j] = b
def queryRow(a):
	sum = 0
	for j in range(0,SET_SPACE):
		sum = sum + matrix[a][j]
	print sum
def queryCol(a):
	sum = 0
	for i in range(0,SET_SPACE):
		sum = sum + matrix[i][a]
	print sum

command = {"SetRow" : setRow, "SetCol" : setCol, 
			"QueryCol" : queryCol, "QueryRow" : queryRow}

for test in test_cases:
	test = test.strip()
	data = test.split(" ")

	if data[0] == "SetRow" or data[0] == "SetCol":
		command[data[0]](int(data[1]),int(data[2]))
	else:
		command[data[0]](int(data[1]))

