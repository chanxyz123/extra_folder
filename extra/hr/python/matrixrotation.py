def rotate(arr,r):
	l = len(arr)
	c = r%l
	i=0
	a = []
	while i<l:
		if i+c>=l:
			a.append(arr[i+c-l])
			i+=1
		else:
			a.append(arr[i+c])
			i+=1
	return a
st = raw_input()
st = st.split()
m = int(st[0])
n = int(st[1])
r = int(st[2])
arr1  =[]
for x in range(0,m):
	arr =[]
	s = raw_input()
	s = s.split()
	for y in range(0,n):
		arr.append(int(s[y]))
	arr1.append(arr)
print arr1
i=0
arr3 = []
if m%2==0:
	while(i<m/2):
		arr2 = []
		for x in range(i,n-i):
			arr2.append(arr1[i][x])
		for x in range(i+1,m-1-i):
			arr2.append(arr1[x][n-1-i])
		j=n-i-1
		while j>=i:
			arr2.append(arr1[n-1-i][j])
			j-=1
		k =m-2-i
		while k>i:
			arr2.append(arr1[k][i])
			k-=1
		arr3.append(arr2)
		i+=1
arr5 = []
l=0
for x in xrange(0,len(arr3)):
	arr3[x] = rotate(arr3[x],r)
	print arr3[x]
	arr4 =[] 
for y in range(0,n):
	arr4.append(arr3[0][y])
arr5.append(arr4)
for x in xrange(0,len(arr3)):
	arr4 = []
	for z in range(n-l,n+m-2-(2*l)):
		if x==0:
			arr5.append([arr3[x][z]])
		else:
			arr4.append(arr3[x][z])
	if x!=0:
		arr5[x].insert(x,arr4)
	i==1
	for w in range((2*(n-l))+m-l-2,(2*(n+m-(2*l)))-4):
		if x==0:
			arr5[i].insert(0,arr3[x][w])
			i+=1
		else:
			arr4.append(arr3[x][w])
	if x!=0:
		arr5[m-2-x].insert(x,arr4)
	l+=2
arr4 = []
for x in xrange(0,n):
	arr4.append(arr3[0][n+m-2+x])
arr5.append(arr4)
print arr5