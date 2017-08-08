#!/bin/python

import sys

def checkBoard(b, n):
    if b[0] != b[1] or b[n - 1] != b[n - 2]:
        return False
    else:
        for i in range(1, n - 1):
            if b[i] != b[i - 1] and b[i] != b[i + 1]:
                return False
            
        return True
        

Q = int(raw_input().strip())
for a0 in xrange(Q):
    n = int(raw_input().strip())
    b = raw_input().strip()
    flag = True
    
    if n == 1:
        if b[0] == "_":
            print "YES"
        else:
            print "NO"
    elif checkBoard(b, n):
        print "YES"
    else:
        if b.count("_") < 1:
            print "NO"
        else:
            start = 'a'
            while start <= 'z':
                if b.count(start.upper()) == 1:
                    flag = False
                    break
            
                start = chr(ord(start) + 1)
            
            if flag:
                print "YES"
            else:
                print "NO"
        