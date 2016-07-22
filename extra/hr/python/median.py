def median(s,x,arr):
    if s=="a":
        arr.append(x)
        if len(arr)-1==0:
            return arr[0]
        else:
            i = len(arr)-1   
            if (len(arr)-1)%2!=0:
                arr.sort()
                if (arr[int(i/2)]+arr[int(i/2)+1])%2==0:
                    return (arr[int(i/2)]+arr[int(i/2)+1])/2
                else:
                    return float(arr[int(i/2)]+arr[int(i/2)+1])/2
            else:
                arr.sort()
                return arr[int(i/2)]
    elif s=="r":
        if len(arr)==0:
            return "Wrong!"
        else:
            if x in arr:
                arr.remove(x)
            else:
                return "Wrong!"
            if len(arr)==0:
                return "Wrong!"
            i = len(arr)-1
            if (len(arr)-1)%2!=0:
                arr.sort()
                if (arr[int(i/2)]+arr[int(i/2)+1])%2==0:
                    return (arr[int(i/2)]+arr[int(i/2)+1])/2
                else:
                    return float(arr[int(i/2)]+arr[int(i/2)+1])/2
            else:
                arr.sort()
                return arr[int(i/2)]
N = int(raw_input())
arr =[]
j=0
if N>1000:
    N1 = N/100;
    N2 = N-N1;
    for i in range(0, N1):
        tmp = raw_input().strip().split(' ')
        s = tmp[0]
        x = int(tmp[1])
        print median(s,x,arr)
    for i in range(0, N2):
        tmp = raw_input().strip().split(' ')
        s = tmp[0]
        x = int(tmp[1])
        print median(s,x,arr)
else:
    for i in range(0, N):
        tmp = raw_input().strip().split(' ')
        s = tmp[0]
        x = int(tmp[1])
        print median(s,x,arr)
    

