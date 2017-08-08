#!/bin/python

import sys

def getRecord(s):
    recordMax = 0
    recordMin = 0
    
    for i in range(1, len(s)):
        if s[i] > max(s[:i]):
            recordMax = recordMax + 1
        elif s[i] < min(s[:i]):
            recordMin = recordMin + 1
    
    return [recordMax, recordMin]

n = int(raw_input().strip())
s = map(int, raw_input().strip().split(' '))
result = getRecord(s)
print " ".join(map(str, result))