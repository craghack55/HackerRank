#!/bin/python

import sys
import numpy as np

if __name__ == '__main__':
    n = int(raw_input())
    student_marks = {}
    for _ in range(n):
        line = raw_input().split()
        name, scores = line[0], line[1:]
        scores = map(float, scores)
        student_marks[name] = scores
        
    student_marks = dict(student_marks)
    
    query_name = raw_input()
    
    print '%.2f' % np.mean(student_marks[query_name])
    