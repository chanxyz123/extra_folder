import time
def permutation(a,l,n):
	if l==n:
		print ''.join(a)
	else:
		for x in range(l,n+1):
			a[l],a[x] = a[x],a[l]
			permutation(a,l+1,n)
			a[l],a[x]=a[x],a[l]
n =  int(raw_input())
a= []
for x in xrange(1,n+1):
	a.append(str(x))
start = time.clock()
permutation(a,0,n-1)
stop = time.clock()
f = open("data.txt",'a')
f.write(str(start-stop))
f.write("\n")