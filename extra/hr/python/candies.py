n = int(raw_input())
arr =[]
for x in range(0,n):
    s = int(raw_input())
    arr.append(s)
total = 1
count = 1
for x in range(0,n-1):
    if arr[x+1]-arr[x]>0:
        count+=1
        total+=count
    else:
        if count!=1:
            count=1
        else:
            count+=1
        total+=count
print total