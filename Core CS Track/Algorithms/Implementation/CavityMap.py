#!/bin/python

import sys

n = int(raw_input().strip())

grid = []
grid_i = 0

for grid_i in xrange(n):
    grid_t = str(raw_input().strip())
    grid.append(grid_t)
    
for i in range (0, len(grid)):
    temp = list(grid[i])
    for j in range(1, len(grid[i]) - 1):
        
        if i != 0 and i != len(grid) - 1:
            if grid[i][j] > grid[i][j + 1] and grid[i][j] > grid[i][j - 1] and grid[i][j] > grid[i + 1][j] and grid[i][j] > grid[i - 1][j]:
                temp[j] = "X"
            
    print "".join(temp)
