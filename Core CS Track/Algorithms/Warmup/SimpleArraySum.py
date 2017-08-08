#!/bin/python

import sys

n = int(raw_input().strip())
arr = map(int, raw_input().strip().split(' '))

arraySum = 0

for i in arr:
    arraySum = arraySum + i
    
print arraySum

