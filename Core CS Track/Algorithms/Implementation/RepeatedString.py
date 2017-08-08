#!/bin/python

import sys


s = raw_input().strip()
n = long(raw_input().strip())

occ = s.count("a")
remainder = n % len(s)

print occ * (n / len(s)) + s[:remainder].count("a")