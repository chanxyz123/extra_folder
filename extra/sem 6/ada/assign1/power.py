import time
def rules(x,y):
    if x==0 and y==0:
        return 0,0
    elif x==1 and y==0 or x==0 and y==1:
        return 1,0
    elif x==1 and y==1:
        return 0,1
def add(arr):
    a =[]
    s,c = rules(arr[len(arr)-1],1)
    a.append(s)
    i=1
    while c==1:
        s,c = rules(arr[len(arr)-1-i],1)
        a.append(s)
        i+=1
    j = len(arr)-1-i
    while j>=0:
        a.append(arr[j])
        j-=1
    a.reverse()
    return a
def stri(a,s):
    st=""
    for x in range(0,len(a)):
        if a[x]==1:
            st+=s[x]
    return st
n = int(raw_input("Enter the number in set ="))
arr=[]
s=[]
for x in range(1,n+1):
    s.append(str(x))
    arr.append(0)
start = time.clock()
for x in range(0,pow(2,n)-1):
    arr = add(arr)
    print stri(arr,s)
stop = time.clock()
print stop-start