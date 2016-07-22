import math
def squre(low,high):
    arr = []
    root = math.sqrt(float(low))
    root1 = root - math.floor(root)
    root2 = int(math.floor(root))+1
    if root1 > 0.0:
        while math.pow(root2,2)<=high:
            arr.append(math.pow(root2,2))
            root2+=1
    else:
        arr.append(math.pow(root2-1,2))
        root2+=1
        while math.pow(root2,2)<=high:
            arr.append(math.pow(root2,2))
            root2+=1
    return arr
test_case =  input()
for x in range(0,test_case):
    interval =  raw_input()
    interval = interval.split()
    print squre(interval[0],interval[1])