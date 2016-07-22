def compare(curr,adg):
	min1,pos1 = min(curr)
	min2,pos2 = min(adg)
	if pos1==pos2:
		if min1<min2:
			adg.remove(min2)
			min2,pos2 = min(adg)
			return min2,pos2
		elif min1>min2:
			curr.remove(min1)
			min1,pos1 = min(curr)
			return min1,pos1
	else:
		return min1,pos1,min2,pos2

def min(l):
	i=1
	pos = 0
	m = l[0]
	while i<len(l):
		if m > l[i]: 
			m = l[i]
			pos  = i
		else:
			continue
	return m,pos

test_case = int(raw_input())
no_of_shops = int(raw_input())
i=0
arr = []
while (i<no_of_shops):
	x = raw_input()
	y = x.split()
	arr.append([int(y[0]),int(y[1]),int(y[2])])
	i = i+1
min1,pos1 = min(curr)