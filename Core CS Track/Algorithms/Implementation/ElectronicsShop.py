#!/bin/python

import sys

def getMoneySpent(keyboards, drives, s):
    combinations = []
    
    for i in keyboards:
        for j in drives:
            combinations.append((i, j))
            
    maxAmount = -1
    
    for keyboard, drive in combinations:
        if (keyboard + drive) <= s:
            if (keyboard + drive > maxAmount):
                maxAmount = keyboard + drive
                
    return maxAmount

    

s,n,m = raw_input().strip().split(' ')
s,n,m = [int(s),int(n),int(m)]
keyboards = map(int, raw_input().strip().split(' '))
drives = map(int, raw_input().strip().split(' '))

#  The maximum amount of money she can spend on a keyboard and USB drive, or -1 if she can't purchase both items
moneySpent = getMoneySpent(keyboards, drives, s)

print(moneySpent)