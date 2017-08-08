#!/bin/python

import sys
from itertools import groupby

students = []

for _ in range(int(raw_input())):
    name = raw_input()
    score = float(raw_input())
    
    students.append((name, score))
    
students = sorted(students, key = lambda t : t[1])
result = []

for i, j in groupby(students, key = lambda t : t[1]):
    result.append(list(j))
    
result = sorted(result[1], key = lambda t : t[0])
  
for i in result:
    print i[0]


    