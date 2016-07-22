def getindex(arr,v):
    for x in range(0,len(arr)):
        if arr[x]> v:
            # print "hello",x
            return x
    return len(arr)
def min(arr):
    arr.sort()
    i = 0
    count= 0
    while i<len(arr):
            count+=1
            # print arr,count
            # print getindex(arr,arr[i]+4)
            if getindex(arr,arr[i]+4):
                i=getindex(arr,arr[i]+4)
            else:
                i+=1
    return count
n = int(raw_input())
arr = map(int,raw_input().split())
print min(arr)