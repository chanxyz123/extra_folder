def function(S):
	R = S[::-1]
	for x in xrange(1,len(S)):
		if abs(ord(S[x]) - ord(S[x-1])) == abs(ord(R[x]) - ord(R[x-1])):
			continue
		else:
			return "Not Funny"
	return "Funny"

test_case = int(raw_input())
for x in xrange(0,test_case):
	S = raw_input()
	print function(S)