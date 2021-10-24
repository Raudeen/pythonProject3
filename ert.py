import time
import datetime
n = 0
start = datetime.datetime.now()
for i in range(1000000000):
	if i % 4 == 0:
		n = n + 1
	else:
		pass
bone = datetime.datetime.now() - start
print(n)
print(f'время работы: {bone}')