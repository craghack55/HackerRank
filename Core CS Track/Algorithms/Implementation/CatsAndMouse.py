#!/bin/python

import sys


q = int(raw_input().strip())
for a0 in xrange(q):
    x,y,z = raw_input().strip().split(' ')
    x,y,z = [int(x),int(y),int(z)]
    
    if abs(z - x) < abs(z - y):
        print "Cat A"
    elif abs(z- x) > abs(z - y):
        print "Cat B"
    else:
        print "Mouse C"