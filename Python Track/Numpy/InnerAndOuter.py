import numpy as np

A = list(map(int, raw_input().split()))
B = list(map(int, raw_input().split()))

print np.inner(A, B)
print np.outer(A, B)