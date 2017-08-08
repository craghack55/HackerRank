#!/bin/python

import sys


q = int(raw_input().strip())
for a0 in xrange(q):
    n = int(raw_input().strip())
    M = []
    flag = True
    for M_i in xrange(n):
        M_temp = map(int,raw_input().strip().split(' '))
        M.append(M_temp)
        
    sumM = [sum(x) for x in M]
    sumBalls = []
    
    for i in range(0, len(M)):
        sums = 0
        for j in range(0, len(M)):
            sums += M[j][i]
            
        sumBalls.append(sums)
        
    flag = False
    
    for i in range(0, len(sumBalls)):
        for j in range(0, len(sumM)):
            flag = False
            if sumM[j] == sumBalls[i]:
                flag = True
                break
        
        
    if flag:
        print "Possible"
    else:
        print "Impossible"
            
            