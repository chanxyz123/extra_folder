def calculate(value,power):
    total = 0
    for x in range(0,power):
        total +=value
    return total
def stones(n,a,b):
    i=0
    arr =[]
    if n%2==0:
        while i<n/2:
            arr.append(calculate(a,n-i-1)+calculate(b,i))
            i+=1
        i=0
        ar =[]
        while i<n/2:
            ar.append(calculate(b,n-i-1)+calculate(a,i))
            i+=1
        ar.reverse()
        for x in range(0,len(ar)):
            arr.append(ar[x])
    elif n==1:
        return arr.append(0)
    else:
        while i<n/2:
            arr.append(calculate(a,n-i-1)+calculate(b,i))
            i+=1
        arr.append(calculate(a,(n-(n-1)/2)-1)+calculate(b,(n-1)/2)) 
        i=0
        ar =[]
        while i<n/2:
            ar.append(calculate(b,n-i-1)+calculate(a,i))
            i+=1
        ar.reverse()
        for x in range(0,len(ar)):
            arr.append(ar[x])
    return set(arr)
test_case = int(raw_input())
for x in range(0,test_case):
    n = int(raw_input())
    a  = int(raw_input())
    b = int(raw_input())
    arr = stones(n,a,b)
    arr =list(arr)
    arr.sort()
    for x in range(0,len(arr)):
        print arr[x],
    print ""