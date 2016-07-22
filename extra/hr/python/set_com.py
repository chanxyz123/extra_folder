x = int(raw_input())
y = int(raw_input())
z = int(raw_input())
n = int(raw_input())
a= []
lis = [x+1,y+1,z+1]
lis.sort()
for i in range(0,x+1):
	for j in range(0,y+1):
		for k in range(0,z+1):
			if (i+j+k) != n:
				t = [i,j,k]
				a = a+[t]	

print a

			 
