#!/bin/python

import sys


n = int(raw_input().strip())
c = map(int,raw_input().strip().split(' '))
i = 0
moves = 0

while(True):
    if i == n - 1:
        break
    elif i == n - 2:
        moves += 1
        i += 1
        continue
    elif c[i + 2] == 0:
        moves += 1
        i += 2
    else:
        moves += 1
        i += 1

print moves