import numpy as np

n = int(raw_input())

result = []

for i in range(n):
    result.append(list(map(int, raw_input().split())))
    
A = np.array(result)

result = []

for i in range(n):
    result.append(list(map(int, raw_input().split())))
    
B = np.array(result)

print np.matmul(A, B)