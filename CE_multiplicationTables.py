for i in range(1,13):
	for j in range(1,13):
		if j == 1:
			print i*j,
		else:
			print "%4s" % str(i*j),
	print ""