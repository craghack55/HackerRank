#!/bin/python

import sys


n = int(raw_input().strip())
arr = map(int, raw_input().strip().split(' '))

arrSum = 0

for i in arr:
    arrSum = arrSum + i
    
print arrSum