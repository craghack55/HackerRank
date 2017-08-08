#!/bin/python

from __future__ import print_function 
import sys

t = int(raw_input().strip())
for a0 in xrange(t):
    n,k = raw_input().strip().split(' ')
    n,k = [int(n),int(k)]
    p = [0 for x in range(1, n + 1)]
    
    if k != 0 and n % (2 * k) != 0:
        print(-1)
    else:
        for i in range(1, n + 1):
            if p[i - 1] == 0:
                p[i - 1] = str(i + k)
                p[i + k - 1] = str(i)
        
        print(' '.join(p))