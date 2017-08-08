#!/bin/python

import sys


n = int(raw_input().strip())
a = []
for a_i in xrange(n):
    a_temp = map(int,raw_input().strip().split(' '))
    a.append(a_temp)
    
primary = 0
secondary = 0

for i in range(0, len(a)):
    primary = primary + a[i][i]
    secondary = secondary + a[i][len(a) - i - 1]
    
print abs(primary - secondary)

