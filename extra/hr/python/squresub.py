def rules(x,y):
    if x==0 and y==0:
        return 0,0
    elif x==1 and y==0 or x==0 and y==1:
        return 1,0
    elif x==1 and y==1:
        return 1,1
def add(arr):
    a =[]
    s,c = rules(arr[len(arr)-1],1)
    a.append(s)
    for x in range(1,len(arr)):
        if c==1:
            s,c = rules(arr[len(arr)-1-x],c)
            a.append(s)
    a.reverse()
    return a
            
def squresub(s):
    i=0
    arr =[]
    for x in range(0,len(s)):
        arr.append(0)
    while len(s)==add(arr):
        for x in range(0,len(s)):
            
n =  int(raw_input())
for x in range(0,n):
    s = raw_input()
    print squresub(s):