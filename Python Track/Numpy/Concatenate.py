import numpy

n,m,p = map(int, raw_input().split())

result = []

for i in range(n + m):
    result.append(list(map(int, raw_input().split())))
    
print numpy.array(result)