#!/bin/python

import sys


n = int(raw_input().strip())
arr = map(int,raw_input().strip().split(' '))

while len(arr) != 0:
    print len(arr)
    
    arr.sort()
    arr = list(map(lambda x : x - arr[0], arr))
    arr = [x for x in arr if x != 0]