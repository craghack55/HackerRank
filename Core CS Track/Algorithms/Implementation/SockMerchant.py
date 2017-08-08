#!/bin/python

import sys
from collections import Counter

n = int(raw_input().strip())
c = map(int,raw_input().strip().split(' '))

occ = Counter(c)
pairs = 0

for key, value in occ.iteritems():
    pairs = pairs + int(value) / int(2)
    
print pairs
