#!/bin/python

import sys
import math

t = int(raw_input().strip())

if t <= 3:
    c = 0
else:
    c = int(math.floor(math.log((t / 3), 2)))

    if c == 0 and t > 3:
        c = 1

v = 3 * (2 ** c)
    
print v - (t - (v - 2))