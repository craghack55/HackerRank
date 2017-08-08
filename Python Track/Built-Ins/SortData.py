from __future__ import print_function
n, m = map(int, raw_input().split())

temp = []

for i in range(n):
    elements = list(map(int, raw_input().split()))
    temp.append(elements)
    
k = int(raw_input())

for i in sorted(temp, key = lambda x : x[k]):
    print(*i, sep = " ")