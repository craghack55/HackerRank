#!/bin/python

import sys

a0, a1, a2 = raw_input().strip().split(' ')
a0, a1, a2 = [int(a0), int(a1), int(a2)]
b0, b1, b2 = raw_input().strip().split(' ')
b0, b1, b2 = [int(b0), int(b1), int(b2)]

scoreA = 0
scoreB = 0

if a0 > b0:
    scoreA = scoreA + 1
elif a0 < b0:
    scoreB = scoreB + 1
    
if a1 > b1:
    scoreA = scoreA + 1
elif a1 < b1:
    scoreB = scoreB + 1
    
if a2 > b2:
    scoreA = scoreA + 1
elif a2 < b2:
    scoreB = scoreB + 1
    
print str(scoreA) + " " + str(scoreB)    
