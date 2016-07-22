def ps(a,x):
	for y in range(1,len(a)):
		v= []
		for z in range(0,len(arr[y])):
			v.append(arr[y][z]*x)
		a.append(v)
	return a
n = int(raw_input("Enter the numer in set"))
arr  = map(int,raw_input().split())
a =[]
a.append([1])
a.append([arr[0]])
for x in range(1,n):
	a = ps(a,arr[x]) 
print a
