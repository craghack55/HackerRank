#!/bin/python

import sys

n, k = raw_input().strip().split(' ')
n, k = [int(n),int(k)]
items = map(int, raw_input().strip().split(' '))
charged = int(raw_input().strip())

actual = (sum(items) - items[k]) / 2

if actual == charged :
    print "Bon Appetit"
else:
    print charged - actual