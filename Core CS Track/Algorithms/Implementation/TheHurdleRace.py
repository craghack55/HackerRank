#!/bin/python

import sys

n,k = raw_input().strip().split(' ')
n,k = [int(n),int(k)]
height = map(int, raw_input().strip().split(' '))
beverages = 0

for h in height:
    if k + beverages < h:
        while k + beverages < h:
            beverages += 1
        
    
print beverages

