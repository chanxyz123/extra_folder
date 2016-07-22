#!/bin/python

import sys
def cavity(arr,i):
    j=1
    while j<(len(arr)-1):
        if arr[i][j]!="X" and arr[i-1][j] !="X" and arr[i][j-1] != "X" and arr[i][j+1]!="X" and arr[i+1][j]!="X":
            if int(arr[i][j]) > int(arr[i][j+1]) and int(arr[i][j]) > int(arr[i][j-1]) and int(arr[i][j]) > int(arr[i-1][j]) and int(arr[i][j]) > int(arr[i+1][j]):
                arr[i] = arr[i].replace(arr[i][j],"X")
                j+=1
            else:
                j+=1
        else:
            j+=1
    return arr[i]
n = int(raw_input().strip())
grid = []
grid_i = 0
for grid_i in xrange(n):
   grid_t = str(raw_input().strip())
   grid.append(grid_t)
# grid = cavity(grid)
i=1
print grid[0]
while i<(len(grid)-1):
    print cavity(grid,i)
    i+=1
if (len(grid)-1)!=0:
    print grid[len(grid)-1]
# for x in range(0,len(grid)):
#     print grid[x]
