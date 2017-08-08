#!/bin/python

import sys


t = int(raw_input().strip())
for a0 in xrange(t):
    n,k = raw_input().strip().split(' ')
    n,k = [int(n),int(k)]
    a = map(int,raw_input().strip().split(' '))
    cancel = "NO"
    absent = 0
    
    for student in a:
        if student > 0:
            absent += 1
            if n - absent < k:
                cancel = "YES"
                break
            
    print cancel
    