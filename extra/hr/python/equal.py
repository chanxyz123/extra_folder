def factor(num):
    five = num/5
    two =(num%5)/2
    if (num%5)%2==0:
        one=0
    else:
        one=1
    return five,two,one
test_case = int(raw_input())
for x in range(0,test_case):
    n = int (raw_input())
    arr =  map(int,raw_input().split())
    arr.sort()
    total =0
    count=0
    extra =0
    a =[]
    for x in xrange(0,len(arr)-1):
        n= arr[x+1]-arr[x]
        a.append(n+extra)
        extra += n
        five,two,one = factor(a[x])
        count+=five
        count+=two
        count+=one
    if sum(a)<=30:
        count=0
        five,two,one = factor(sum(a))
        print five,two,one
        count+=five
        print count,five
        count+=two
        print count,two
        count+=one
        print count,one
        print count,sum(a)
    else:
        print count,sum(a)