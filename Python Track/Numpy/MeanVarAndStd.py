import numpy as np

n, m = map(int, raw_input().split())
result = []

for i in range(n):
    result.append(list(map(int, raw_input().split())))
    
    
result = np.array(result)

print np.mean(result, axis = 1)
print np.var(result, axis = 0)
print np.std(result, axis = None) 
