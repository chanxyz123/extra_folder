def count(N):
	num = 0
	check = N
	if N < 10:
		num = num +1
		return num
	else:
		while True:
			if check < 10:
				if (N % check)==0:
					num = num + 1
				break
			else:
				while (check/10)>0:
					n = check % 10
					if n==0:
						check = check/10
						continue
					elif (N % n)==0:
						num = num + 1
						check = check/10
						continue
					else:
						check = check/10
						continue
		return num
test_case  = int(raw_input())
for x in xrange(0,test_case):
	N = int(raw_input())
	num = count(N)
	print num