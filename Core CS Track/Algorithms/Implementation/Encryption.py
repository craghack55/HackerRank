#!/bin/python

import sys
import math

s = raw_input().strip()
L = len(s)
r = 0
c = 0

for row in range(int(math.floor(math.sqrt(L))), int(math.ceil(math.sqrt(L))) + 1):
    
    if row * row >= L:
        r = row
        c = row
        break
    elif row * (row + 1) >= L and row + 1 <= math.ceil(math.sqrt(L)):
        r = row
        c = row + 1
        
    
grid = []

s = s + " " * (r * c - L)
result = ""

for i in range(0, c):
    for j in range(i, len(s), c):
        if s[j] != " ":
            result += s[j]
            
    result += " "
            
            
print result
    



