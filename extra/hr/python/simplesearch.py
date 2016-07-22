def binarySearch (arr, l, r, x):
 
    # Check base case
    if r >= l:
 
        mid = l + (r - l)/2
 
        # If element is present at the middle itself
        if arr[mid] == x:
            return mid
         
        # If element is smaller than mid, then it can only
        # be present in left subarray
        elif arr[mid] > x:
            return binarySearch(arr, l, mid-1, x)
 
        # Else the element can only be present in right subarray
        else:
            return binarySearch(arr, mid+1, r, x)
 
    else:
        # Element is not present in the array
        return -1
test_case = int(raw_input())
for x in range(0,test_case):
    n,q = map(int,raw_input().split())
    arr = map(float,raw_input().split())
    arr.sort()
    for y in range(0,q):
        i = float(raw_input())
        count = 0
        result = binarySearch(arr,0,n-1,i)
        print n-(result+1)