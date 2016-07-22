def largest(a):
	temp = a.pop()
	temp1 =a.pop()
	while 1:
		if temp1!=temp:
			return temp1
		else:
			temp1 = a.pop()

n= int(raw_input())
arr = raw_input()
a = arr.split(" ")
a = (map(int,a))
a.sort()
second = largest(a)
print second



