

import sys
import os
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
	os.path.getsize(test)
test_cases.close()
