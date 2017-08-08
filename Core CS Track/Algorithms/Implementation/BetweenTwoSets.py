#!/bin/python

import sys


n,m = raw_input().strip().split(' ')
n,m = [int(n),int(m)]
a = map(int,raw_input().strip().split(' '))
b = map(int,raw_input().strip().split(' '))

a = sorted(a)
b = sorted(b)
result = []
flag1 = True
flag2 = True
counter = 1

while counter <= b[-1]:
    flag1 = True
    flag2 = True
    
    for i in a:
        if counter % i != 0:
            counter = counter + 1
            flag1 = False
            break
        else:
            continue
    
    if flag1:
        for i in b:
            if i % counter != 0:
                counter = counter + 1
                flag2 = False
                break
            else:
                continue
        
        if flag2:
            result.append(counter)
            counter = counter + 1

                        
print len(result)
        




