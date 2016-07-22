def function(A,B):
	arr1 = []
	arr2 = []
	for x in xrange(65,91):
		arr1.append([x,0])
		arr2.append([x,0])
	i=0
	while i<len(A):
		arr1[ord(A[i])-65][1] = arr1[ord(A[i])-65][1]+1
		arr2[ord(B[i])-65][1] = arr2[ord(B[i])-65][1]+1
		i =i+1
	count = 0
	for x in xrange(0,26):
		if arr1[x][1]==arr2[x][1]:
			count = count + arr2[x][1]
		elif arr1[x][1]>arr2[x][1]:
			count = count + arr2[x][1]
		else:
			count =count + arr1[x][1]
	return count

A = raw_input()
B = raw_input()
print function(A,B)