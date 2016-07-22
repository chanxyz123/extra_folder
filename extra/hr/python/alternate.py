def function(S):
	i = 1
	s = S[0]
	count = 0
	while i<len(S):
		if S[i]==s:
			count = count +1
			i = i+1
			continue
		else:
			s = S[i]
			i= i+1
			continue
	return count
test_case = int(raw_input())
for x in xrange(0,test_case):
	S = raw_input()
	print function(S)
