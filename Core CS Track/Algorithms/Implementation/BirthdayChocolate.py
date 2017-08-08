#!/bin/python

import sys

def getWays(squares, d, m):
    ways = 0
    
    for i in range(0, len(squares) - (m - 1)):
        seqSum = 0
        
        for j in range(0, m):
            seqSum = seqSum + squares[i + j]
            
        if seqSum == d:
            ways = ways + 1
    
    return ways
    

n = int(raw_input().strip())
s = map(int, raw_input().strip().split(' '))
d,m = raw_input().strip().split(' ')
d,m = [int(d),int(m)]
result = getWays(s, d, m)
print(result)