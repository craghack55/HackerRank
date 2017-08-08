#!/bin/python

import sys        

n = int(raw_input().strip())
steps = str(raw_input().strip())
steps = list(steps)
valleys = 0
height = 0

for step in steps:
    if step == 'D':
        direction = -1
    else:
        direction = 1
        
    if height >= 0 and height + direction < 0:
        valleys = valleys + 1
    
    height = height + direction
        

print valleys