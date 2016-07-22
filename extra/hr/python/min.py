def sorting(a):
	temp = []
	l =[]
	for i in range(0,len(a)):		
		if i == 0:
			l = l+[a[i]]
		else:
			n = i
			l = l+[a[n]]
			while(n>0):
				if l[n-1][1] > l[n][1]:
					temp = l[n-1]
					l[n-1] = l[n]
					l[n] =temp
					n = n-1
				else:
					n =0
	return l
def ssort(a):
	l = []
	arr = sorting(a)
	arr.reverse()
	i = len(arr)
	temp = arr.pop()
	temp1 = arr.pop()
	while 1:
		if temp1[1]!=temp[1]:
			l = l + [temp1]
			while 1:
				if len(arr)!=0:
					temp2 = arr.pop()
					if temp2[1]==temp1[1]:
						l = l+[temp2]
					else:
						return l
				else:
					return l		
		else:
			temp = temp1
			temp1 = arr.pop()
	return l
k = int(raw_input())
a = []
for i in range(0,k):
	name = raw_input()
	number = float(raw_input())
	a = a + [[name,number]] 
lis =  ssort(a)
i = len(lis)
while i>0:
	print lis[i-1][0]
	i =i-1