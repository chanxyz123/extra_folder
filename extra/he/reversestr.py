test_case = int(raw_input())
i=0
while i<test_case:
	st = raw_input()
	chandu = list(st)
	chandu.reverse()
	j=0
	while j<len(chandu):
		print chandu[j],
		j = j+1
	print ""
	i=i+1