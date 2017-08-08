#!/bin/python

import sys

n,k = raw_input().strip().split(' ')
n,k = [int(n),int(k)]
a = map(int, raw_input().strip().split(' '))

numOfPairs = 0

for i in range(0, n):
    for j in range(0, n):
        if i < j and (a[i] + a[j]) % k == 0:
            numOfPairs = numOfPairs + 1
        
print numOfPairs
    
