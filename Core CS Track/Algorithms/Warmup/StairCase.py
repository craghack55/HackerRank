#!/bin/python

import sys


n = int(raw_input().strip())

for i in range(0, n):
    temp = ""
    for spaces in range(0, n - i - 1):
        temp = temp + " "
    
    for squares in range(0, i + 1):
        temp = temp + "#"
        
    print temp
