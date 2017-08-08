#!/bin/python

import sys

def saveThePrisoner(n, m, s):
    result = (s + (m % n) - 1) % n
    
    if result == 0:
        return n
    else:
        return result

t = int(raw_input().strip())
for a0 in xrange(t):
    n, m, s = raw_input().strip().split(' ')
    n, m, s = [int(n), int(m), int(s)]
    result = saveThePrisoner(n, m, s)
    print(result)