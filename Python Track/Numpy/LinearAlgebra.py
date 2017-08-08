import numpy as np

n = int(raw_input())
result = []

for i in range(n):
    result.append(list(map(float, raw_input().split())))
    
    
result = np.array(result)

print np.linalg.det(result)