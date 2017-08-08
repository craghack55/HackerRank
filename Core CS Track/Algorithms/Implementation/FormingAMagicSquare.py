#!/bin/python

import sys

s = []
for s_i in xrange(3):
    s_temp = map(int, raw_input().strip().split(' '))
    s.append(s_temp)

costs = []
allms = []

ms1 = [[8, 1, 6], [3, 5, 7], [4, 9, 2]]
ms2 = [[6, 1, 8], [7, 5, 3], [2, 9, 4]]
ms3 = [[4, 3, 8], [9, 5, 1], [2, 7, 6]]
ms4 = [[2, 7, 6], [9, 5, 1], [4, 3, 8]]
ms5 = [[2, 9, 4], [7, 5, 3], [6, 1, 8]]
ms6 = [[4, 9, 2], [3, 5, 7], [8, 1, 6]]
ms7 = [[6, 7, 2], [1, 5, 9], [8, 3, 4]]
ms8 = [[8, 3, 4], [1, 5, 9], [6, 7, 2]]

allms.append(ms1)
allms.append(ms2)
allms.append(ms3)
allms.append(ms4)
allms.append(ms5)
allms.append(ms6)
allms.append(ms7)
allms.append(ms8)

for ms in allms:
    cost = 0
    for i in range(0, len(s), 1):
        for j in range(0 , len(s), 1):
            cost += abs(s[i][j] - ms[i][j])
            
    costs.append(cost)

print min(costs)