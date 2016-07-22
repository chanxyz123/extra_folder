def index(arr,i):
    total =0
    for x in range(0,i):
        total+=arr[x]
    return total
def check(arr):
    total = 0
    for x in range(0,len(arr)):
        total+=arr[x]
    print total
    for x in range(0,len(arr)):
        print index(arr,x),total-arr[x]-index(arr,x),x
        if index(arr,x)==total-arr[x]-index(arr,x):
            return "YES"
    return "NO"
test_case =  int(raw_input())
for x in range(0,test_case):
    n = int(raw_input())
    s = raw_input()
    s=s.split()
    arr = []
    for y in range(0,n):
        arr.append(int(s[y]))
    print check(arr)