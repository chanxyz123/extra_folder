def count(N):
	if N==0:
		num = 1
		return num
	else:
		i=1
		num = 1
		while i<=N:
			if (i % 2)==0:
				num = num+1
				i =i+1
			else:
				num = num * 2
				i =i+1
		return num

test_case = int(raw_input())
for x in xrange(0,test_case):
	N = int(raw_input())
	num = count(N)
	print num