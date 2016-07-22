def fact(x):
	if x == 0:
		temp = 1
	elif x== 1:
		temp=1
	else:
		temp = x*fact(x-1)
	return temp

t = fact(4)
print t 