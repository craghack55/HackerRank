#!/bin/python

import sys


x1,v1,x2,v2 = raw_input().strip().split(' ')
x1,v1,x2,v2 = [int(x1),int(v1),int(x2),int(v2)]

velDiff = v1 - v2
disDiff = x2 - x1

if velDiff <= 0:
    print "NO"
else:
    if disDiff >= velDiff:
        if disDiff % velDiff == 0:
            print "YES"
        else:
            print "NO"
    else:
        if velDiff % disDiff == 0:
            print "YES"
        else:
            print "NO"