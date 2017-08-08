#!/bin/python

import sys


h = map(int, raw_input().strip().split(' '))
word = raw_input().strip()
longest = 0

for letter in word:
    if h[ord(letter) - 97] > longest:
        longest = h[ord(letter) - 97]
        

print len(word) * longest