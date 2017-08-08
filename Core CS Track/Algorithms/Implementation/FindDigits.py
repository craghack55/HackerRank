#!/bin/python

import sys


t = int(raw_input().strip())
for a0 in xrange(t):
    n = int(raw_input().strip())
    s = list(str(n))
    counter = 0
    for i in s:
        if int(i) != 0 and n % int(i) == 0:
            counter += 1
            
    print counter