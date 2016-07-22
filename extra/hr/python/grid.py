def sort(arr):
    for x in range(0,len(arr)):
        arr[x].sort()
    print arr
    arr1 =[]
    for x in range(0,len(arr)):
    	a =[]
        for y in range(0,len(arr)):
            a.append(arr[y][x])
        # print a
        arr1.append(a)
    # print arr1
    for x in range(0,len(arr)):
        arr1[x].sort()
    arr2 =[]
    for x in range(0,len(arr)):
    	a1 =[]
        for y in range(0,len(arr)):
            a1.append(arr1[y][x])
        arr2.append(''.join(a1))
    return arr2

test_case = int(raw_input())
for x in range(0,test_case):
    n = int(raw_input())
    arr= []
    for y in range(0,n):
        s = raw_input()
        s= list(s)
        arr.append(s)
    arr1 = sort(arr)
    for z in range(0,len(arr)):
        print arr1[z]