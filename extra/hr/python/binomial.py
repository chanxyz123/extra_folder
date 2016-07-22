import math
def fac(n1,n2):
	if n2==n1:
		return n1
	else:
		return n2*fac(n1,n2-1) 
def coe(n,k):
	if n-k>k:
		return fac(n-k+1,n)/fac(1,k)
	else:
		return fac(k+1,n)/fac(1,n-k)

s = raw_input()
s = s.split()
print fac(1,4)
print coe(4,2)
print  int(math.pow(int(s[0]),int(s[3])))
print int(math.pow(float(s[1]),float(int(s[2])-int(s[3]))))
print coe(int(s[2]),int(s[3]))
print int(math.pow(float(s[0]),float(s[3])))*coe(int(s[2]),int(s[3]))*int(math.pow(float(s[1]),float(int(s[2])-int(s[3]))))