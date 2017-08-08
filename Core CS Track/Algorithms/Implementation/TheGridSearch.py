#!/bin/python

import sys
import re

def checkPattern(start, g, p, i, c):
    for j in range(1, len(p)):
        end = start + c
        if g[i + j][start:end] != p[j]:
            return False
        
    return True

def gridSearch(g, p, i, c):
    
    m = re.compile("[" + p[0] + "]")
    matches = m.finditer(g[i])
    
    for k in matches:
        if checkPattern(k.start(), g, p, i, c):
            return True
    
    return False


t = int(raw_input().strip())
for a0 in xrange(t):
    R,C = raw_input().strip().split(' ')
    R,C = [int(R),int(C)]
    G = []
    G_i = 0
    
    for G_i in xrange(R):
        G_t = str(raw_input().strip())
        G.append(G_t)
    r,c = raw_input().strip().split(' ')
    r,c = [int(r),int(c)]
    P = []
    P_i = 0
    
    for P_i in xrange(r):
        P_t = str(raw_input().strip())
        P.append(P_t)

    flag = False

    for i in range(0, len(G) - len(P) + 1):
        if gridSearch(G, P, i, c):
            flag = True
            break

    if flag:
        print "YES"
    else:
        print "NO"