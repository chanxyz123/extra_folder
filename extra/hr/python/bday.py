#!/bin/python

import sys
def mini(b,w,x,y,z):
    if x>y and x>z:
        return w*y+b*(y+z)
    elif y>x and y>z:
        return b*x+w*(x+z)
    elif z>x and z>y:
        return b*x+w*y
    elif x<y and y==z or y<x and x==z or x==y and y==z:
        return b*x + w*y
t = int(raw_input().strip())
for a0 in xrange(t):
    b,w = raw_input().strip().split(' ')
    b,w = [int(b),int(w)]
    x,y,z = raw_input().strip().split(' ')
    x,y,z = [int(x),int(y),int(z)]
    print min(w*y+b*(y+z),b*x + w*y,b*x+w*(x+z))
