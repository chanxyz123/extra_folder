def function(A,B):
	arr = []
	for x in xrange(97,123):
		arr.append([x,0])
	i=0
	while i<len(A):
		arr[ord(A[i])-97][1] = arr[ord(A[i])-97][1]+1
		i=i+1
	i=0
	while i<len(B):
		if arr[ord(B[i])-97][1]!=0:
			return "YES"
		else:
			i = i+1
			continue
	return "NO"

test_case =int(raw_input())
for x in xrange(0,test_case):
	A = raw_input()
	B = raw_input()
	print function(A,B)