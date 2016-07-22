def check(arr,p,q):
    count = 0
    a = []
    for x in range(0,max(abs(max(arr)-p),abs(p-min(arr)),abs(max(arr)-q),abs(q-min(arr)))):
        a.append(0)
    c = []
    for x in range(p,q+1):
        b = []
        for y in range(0,len(arr)):
            b.append(abs(arr[y]-x))
            # print b
        c.append([x,min(b)])
        a[min(b)]+=1
    for x in xrange(0,len(a)):
        if 0 in a:
            a.remove(0)
    m =  min(a)
    # print a,c,m
    cc = []
    for x in range(0,len(a)):
        if m==a[x]:
            cc.append(x)
    d = []
    m = max(cc)
    for x in range(0,len(c)):
        if m==c[x][1]:
            d.append(c[x][0])
            # print d
    return max(d)
n = int(raw_input())
arr = map(int,raw_input().split())
p,q = map(int,raw_input().split())
print check(arr,p,q)