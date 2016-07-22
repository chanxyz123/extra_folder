S = raw_input()
arr = []
for x in xrange(97,123):
	arr.append([x,0])
i=0
while i<len(S):
	arr[ord(S[i])-97][1] = arr[ord(S[i])-97][1]+1
	i=i+1
i=0
count = 0
while i<len(arr):
	if (arr[i][1]%2)!=0 :
		count = count +1
		i=i+1
		continue
	else:
		i=i+1
		continue
if count <= 1:
	print "YES"
else:
	print "NO"

