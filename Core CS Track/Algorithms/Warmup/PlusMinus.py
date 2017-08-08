#!/bin/python

import sys


n = int(raw_input().strip())
arr = map(int,raw_input().strip().split(' '))

n = 0
p = 0
z = 0
size = float(len(arr))

for i in arr:
    if i > 0:
        p = p + 1
    elif i < 0:
        n = n + 1
    else:
        z = z + 1
        
print p / size
print n / size
print z / size