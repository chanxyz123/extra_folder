temp = int(raw_input())
a = []
for i in range(0,temp):
	temp1 = raw_input()
	t = temp1.split(" ")
	if t[0]=='insert':
		a.insert(int(t[1]),int(t[2]))
	elif t[0]=='remove':
		a.remove(int(t[1]))
	elif t[0]=='append':
		a.append(int(t[1]))
	elif t[0]=='sort':
		a.sort()
	elif t[0]=='pop':
		value = a.pop()
	elif t[0] == 'reverse':
		a.reverse()
	elif t[0]=='print':
		print a 
