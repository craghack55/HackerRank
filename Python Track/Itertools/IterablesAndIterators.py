import itertools
import sys

n = int(raw_input())
s = raw_input().split()
k = int(raw_input())

combs = list(itertools.combinations(s, k))
allCombs = len(combs)
result = 0

for comb in combs:
    if "a" in comb:
        result += 1
        
print result/allCombs