#!/bin/python

import sys


n = int(raw_input().strip())
A = map(int,raw_input().strip().split(' '))

distances = []

for i in range(0, len(A) - 1):
    for j in  range(i + 1, len(A)):
        if A[i] == A[j]:
            distances.append(abs(i - j))
            

if len(distances) != 0:
    print min(distances)
else:
    print -1