#!/bin/python

import sys


N = int(raw_input().strip())
B = map(int,raw_input().strip().split(' '))
breads = 0
odds = 0

for i in range(N):
    if B[i] % 2 != 0:
        odds += 1

for i in range(N):
    if B[i] % 2 != 0:
        if i != N - 1:
            B[i] += 1
            B[i + 1] += 1
        else:
            B[i] += 1
            B[i - 1] += 1
            
        breads += 2
    
if odds % 2 == 0:
    print breads
else:
    print "NO"
