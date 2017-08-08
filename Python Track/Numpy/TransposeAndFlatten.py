import numpy as np

n, m = map(int, raw_input().split())
result = []

for i in range(n):
    result.append(list(map(int, raw_input().split())))
    
    
result = np.array(result)

print np.transpose(result)
print result.flatten()
