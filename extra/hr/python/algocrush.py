n,m = map(int,raw_input().split())
arr= []
for x in range(0,n):
    arr.append(0)
for x in range(0,m):
    i,j,v = map(int,raw_input().split())
    for y in range(i-1,j):
        arr[y]+=v
print max(arr)