#!/bin/python

import sys


s = raw_input().strip()
t = raw_input().strip()
k = int(raw_input().strip())

if len(s) > len(t):
    marker = len(t)
    
    for i in range(0, len(t)):
        if s[i] == t[i]:
            marker -= 1
        else:
            break    
    
    if k >= len(s) - len(t) + marker * 2 and k != 2:
        print "Yes"
    else:
        print "No"
    
elif len(s) == len(t):
    marker = len(t)
    
    for i in range(0, len(t)):
        if s[i] == t[i]:
            marker -= 1
        else:
            break
    
    if marker != 0:
        if k >= marker * 2:
            print "Yes"
        else:
            print "No"
    else:
        if k >= len(s) * 2:
            print "Yes"
        else:
            if k % 2 == 0:
                print "Yes"
            else:
                print "No"
    
elif len(s) < len(t):
    marker = len(s)
    
    for i in range(0, len(s)):
        if s[i] == t[i]:
            marker -= 1
        else:
            break
        
    result = len(t) - len(s) + marker * 2 
    
    if k >= result and k != 2 and (result % 2 == k % 2):
        print "Yes"
    else:
        print "No"