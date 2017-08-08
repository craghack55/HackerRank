#!/bin/python

import sys
import itertools


n,m = raw_input().strip().split(' ')
n,m = [int(n), int(m)]
topic = []
topic_i = 0

for topic_i in xrange(n):
   topic_t = str(raw_input().strip())
   topic.append(topic_t)
   
   
comb = itertools.combinations(topic, 2)

temp = []

for i in comb:
   s = 0
   for j in i:
      s += int(i[0]) + int(i[1])
      
   
   if len(str(s)) < m:
      zeros = m - len(str(s))
   else:
      zeros = 0
      
   temp.append(m - str(s).count("0") - zeros)

result = max(temp)

print result
print temp.count(result)
   
