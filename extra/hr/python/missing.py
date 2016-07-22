def max(arr):
    m = -10000
    for x in range(0,len(arr)):
        if m<arr[x]:
            m = arr[x]
    return m
def array(arr):
    a = []
    for x in range(min(arr),max(arr)+1):
        a.append(0)
    return a
def min(arr):
    m = 100000
    for x in range(0,len(arr)):
        if m > arr[x]:
            m = arr[x]
    return m
def check(arr1,arr2):
    a1 = array(arr1)
    a2 = array(arr2)
    for x in range(0,len(arr1)):
        a1[arr1[x]-min(arr1)]+=1
    for x in range(0,len(arr2)):
        a2[arr2[x]-min(arr1)]+=1
    count = []
    for x in range(min(arr1),max(arr1)+1):
        if a1[x-min(arr1)]!=a2[x-min(arr1)]:
            count.append(x)
    return list(set(count))
n = int(raw_input())
s1 = raw_input()
s1 = s1.split()
print len(s1)
arr1 = []
arr2 = []
for x in range(0,n):
    arr1.append(int(s1[x]))
m = int(raw_input())
s2 = raw_input()
s2 = s2.split()
for x in range(0,m):
    arr2.append(int(s2[x]))
arr = check(arr1,arr2)
for x in range(0,len(arr)):
    print arr[x],