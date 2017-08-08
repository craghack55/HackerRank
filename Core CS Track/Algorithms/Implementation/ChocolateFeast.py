#!/bin/python

import sys


t = int(raw_input().strip())
for a0 in xrange(t):
    n,c,m = raw_input().strip().split(' ')
    n,c,m = [int(n),int(c),int(m)]

    a = n / c
    total = a
    
    while a >= m:
        total += a / m
        a = a % m + a / m
        
        
    print total
    