def array():
    a = []
    for x in range(0,26):
        a.append(0)
    return a
def count(arr):
    i=0
    arr1= []
    while i<len(arr):
        arr1.append(array())
        for x in range(0,len(arr[i])):
            arr1[i][ord(arr[i][x])-97]+=1
        i+=1
    print arr1
    c=0
    i=0
    a = array()
    while i<26:
        j=0
        while j <len(arr1):
            if arr1[j][i]!=0:
                a[i]+=1
                j+=1
            else:
                j+=1
        i+=1
    for x in range(0,26):
        if a[x]==len(arr):
            c+=1
    return c
test_case =  int(raw_input())
arr = []
for x in range(0,test_case):
    s = raw_input()
    arr.append(s)
print count(arr)
                