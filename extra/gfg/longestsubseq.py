def function(arr):
	sub = 0
	for x in xrange(0,len(arr)):
		count = 0
		for y in range(1,len(arr)):
			if arr[x] < arr[y]:
				count = count +1
			else:
				continue
		if sub <count:
			sub = count
		else:
			continue
	return sub-1
arr_size = int(raw_input())
arr =[]
sub = []
for x in xrange(0,arr_size):
	arr.append(int(raw_input()))
print function(arr)