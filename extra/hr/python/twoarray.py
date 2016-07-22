def count(a,b,n,k):
    a.sort()
    b.sort()
    b.reverse()
    print a,b
    for x in range(0,n):
        if a[x]+b[x]<k:
            return "NO"
    return "YES"
test_case = int(raw_input())
for x in range(0,test_case):
    n,k = map(int,raw_input().split())
    a = map(int,raw_input().split())
    b = map(int,raw_input().split())
    print count(a,b,n,k)