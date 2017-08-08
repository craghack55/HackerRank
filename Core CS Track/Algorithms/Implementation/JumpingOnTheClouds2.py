#!/bin/python

import sys


n,k = raw_input().strip().split(' ')
n,k = [int(n),int(k)]
c = map(int,raw_input().strip().split(' '))
e = 100
i = 0

while (True):
    l = (i + k) % n
    e -= 1
    
    if c[l] == 1:
        e -= 2
    
    if l == 0:
        break
    else:
        i = l
    
print e
        
