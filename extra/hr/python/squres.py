import math
def squre(low,high):
    count = 0
    root = math.sqrt(low)
    root1 = root - math.floor(root)
    root2 = int(math.floor(root))+1
    if root1 > 0.0:
        while math.pow(root2,2)<=high:
            count +=1
            root2+=1
    elif root1 == 0.0:
        count+=1
        root-=1
        while math.pow(root2,2)<=high:
            count+=1
            root2+=1    
    return count
test_case =  int(raw_input())
arr = []
for x in range(0,test_case):
    interval =  raw_input()
    interval = interval.split()
    arr.append(squre(int(interval[0]),int(interval[1])))
for x in xrange(0,test_case):
    print arr[x]