import itertools
import sys
from operator import itemgetter

k, m = map(int, raw_input().split())
allLists = []

for i in range(0, k):
    lst = list(map(int, raw_input().split()))
    allLists.append(lst[1:])
    
combs = itertools.product(*allLists)
results = []
counter = 0

for comb in combs:
    temp = 0
    for i in comb:
        temp += i * i
        
    results.append(temp % m)
    counter += 1
    
print max(results)