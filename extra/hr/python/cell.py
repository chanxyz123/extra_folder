def connected(arr,i,j):
    if j+1<len(arr[i]):
        if arr[i][j+1]==1:
            arr[i][j+1] = 'X'
            return 1+connected(arr,i,j+1)
    if i+1<len(arr):
        if arr[i+1][j]==1:
            arr[i+1][j] = 'X'
            return 1+connected(arr,i+1,j)
    if j-1>=0:
        if arr[i][j-1]==1:
            arr[i][j-1] = 'X'
            return 1+connected(arr,i,j-1)
    if i-1>=0:
        if arr[i-1][j]==1:
            arr[i-1][j] = 'X'
            return 1+connected(arr,i-1,j)
    if j+1<len(arr[i]) and i+1<len(arr):
        if arr[i+1][j+1]==1:
            arr[i+1][j+1] = 'X'
            return 1+connected(arr,i+1,j+1)
    if j-1>=0 and i-1>=0:
        if arr[i-1][j-1]==1:
            arr[i-1][j-1] = 'X'
            return 1+connected(arr,i-1,j-1)
    else:
        return 1
    
m =  int(raw_input())
n =  int(raw_input())
arr =[]
for x in range(0,m):
    a = map(int,raw_input().split())
    arr.append(a)
m =-100000000
for x in range(0,len(arr)):
    for y in range(0,len(arr[x])):
        if arr[x][y]==1:
            count = connected(arr,x,y)
            print count
            if m <count:
                m = count
print m