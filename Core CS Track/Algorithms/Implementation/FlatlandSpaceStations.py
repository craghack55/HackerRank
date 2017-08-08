#!/bin/python

import sys
import bisect

n,m = raw_input().strip().split(' ')
n,m = [int(n),int(m)]
c = map(int,raw_input().strip().split(' '))
distances = []
c = sorted(c)

for i in range(n):
    if i in c:
        distances.append(0)
    else:
        location = bisect.bisect_left(c, i)
        if location == 0:
            distances.append(abs(i - c[0]))
        elif location == len(c):
            distances.append(abs(i - c[location - 1]))
        else:
            a = abs(i - c[location])
            b = abs(i - c[location - 1])
            distances.append(min(a, b))
    
print max(distances)