#!/bin/python

import sys


a,b,c,d,e = raw_input().strip().split(' ')
a,b,c,d,e = [int(a),int(b),int(c),int(d),int(e)]

arr = [a, b, c, d, e]

print str(sum(arr) - max(arr)) + " " + str(sum(arr) - min(arr)) 
    

