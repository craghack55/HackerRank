#!/bin/python

import sys


n = int(raw_input().strip())
height = map(int,raw_input().strip().split(' '))

tallest = max(height)
maxNumOfCandles = 0

for i in height:
    if i == tallest:
        maxNumOfCandles = maxNumOfCandles + 1
        
print maxNumOfCandles

