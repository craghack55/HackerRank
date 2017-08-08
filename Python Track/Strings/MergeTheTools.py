#!/bin/python

import sys

def merge_the_tools(string, k):
    for i in range(0, len(string), k):
        t = string[i : i + k]
        print "".join(list(sorted(set(t), key = t.index)))
        
    