def max(arr,k):
    m=-1111111
    for x in range(k,len(arr)):
        if m < arr[x]:
            m = arr[x]
    return m
def find(arr,k,v):
    for x in range(k,len(arr)):
        if arr[x]==v:
            # print x,v
            return x
    return k
def larg(arr,k):
    if k==0:
        return arr
        # for x in range(0,len(arr)):
            # print arr[x],
    else:
        if k >n:
            k = n
            arr.sort()
            arr.reverse()
        else:
            z=0
            for x in range(0,n):
                # print "hello"
                # print find(arr,x,a[x])
                # print max(arr,x)
                if arr[x]!=max(arr,x):
                    # print "hello"
                    y = find(arr,x,max(arr,x))
                    # print arr[y]
                    temp = arr[x] 
                    # print temp
                    arr[x] = arr[y]
                    # print arr[x] 
                    arr[y] =temp
                    z+=1 
                if z>=k:
                    break
                    # print arr[y]
        return arr
n,k = map(int,raw_input().split())
arr = map(int,raw_input().split())
arr1 = larg(arr,k)  
for x in range(0,len(arr1)):
    print arr1[x],