#!/bin/python

import sys
import math
def encryption(s):
    s = s.replace(" ","")
    l= len(s)
    arr = []
    c =  math.sqrt(l)
    a = int(math.floor(c))
    b = int(math.ceil(c))
    ar = list(s)
    for x in range(0,((a*b)-l)):
        ar.append(" ")
    s = ''.join(ar)
    k = b
    i=0
    for x in range (0,a):
        arr.append(s[i:b])
        i = b
        b +=k
    print arr
    arr2 = []
    for y in range(0,k):
        arr1 = []
        for x in range (0,a):
            if arr[x][y]:
                arr1.append(arr[x][y])
        arr2.append(''.join(arr1))
    return arr2
s = raw_input().strip()
arr =  encryption(s)
for x in range(0,len(arr)):
    print arr[x],