def mincost(a1,a2,y,x,index,v):
    print index
    if index == v:
        return 0
    if len(a1)!=0 and len(a2)!=0:
        if a1[0]>a2[0]:
            ele = a1[0]
            a1.remove(a1[0])
            return mincost(a1,a2,y,x+1,index+1,v)+(ele*y)
        elif a1[0]<a2[0]:
            ele = a2[0]
            a2.remove(a2[0])
            return mincost(a1,a2,y+1,x,index+1,v)+(ele*x)
        elif a1[0]==a2[0]:
            ele = a1[0]
            a1.remove(a1[0])
            return mincost(a1,a2,y,x+1,index+1,v)+(ele*y)
    elif len(a1)==0 and len(a2)!=0:
        ele = a2[0]
        a2.remove(a2[0])
        return mincost(a1,a2,y+1,x,index+1,v)+(ele*x)
    elif len(a1)!=0 and len(a2)==0:
        ele = a1[0]
        a1.remove(a1[0])
        return mincost(a1,a2,y,x+1,index+1,v)+(ele*y)
    
test_case = int(raw_input())
for x in range(0,test_case):
    m,n = map(int,raw_input().split())
    a1 = map(int,raw_input().split())
    a2 = map(int,raw_input().split())
    a1.sort()
    a2.sort()
    a1.reverse()
    a2.reverse()
    i=j=1
    index= 0
    v = m+n-2
    if v<=1000:
        print mincost(a1,a2,i,j,index,v)%1000000007
    else:
        v=998
        total = mincost(a1,a2,i,j,index,v)
        v=m+n-1000
        print (total+mincost(a1,a2,i,j,index,v))%1000000007     
        