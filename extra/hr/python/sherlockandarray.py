def left(arr,index):
    if index==0:
        return 0
    else:
        count = 0
        for x in range(0,index):
            count +=arr[x]
        return count
def right(arr,index):
    if index==(len(arr)-1):
        return 0
    else:
        count =0
        for x in range(index+1,len(arr)):
            count+=arr[x]
        return count
def array(arr):
    for x in range(0,len(arr)):
        if left(arr,x)==right(arr,x):
            return "YES"
    return "NO"
test_case = int(raw_input())
for x in range(0,test_case):
    n= int(raw_input())
    s = raw_input()
    s = s.split()
    arr= []
    for x in range(0,len(s)):
        arr.append(int(s[x]))
    print array(arr)