import numpy as np

a = list(map(float, raw_input().split()))
a = np.array(a)

print a[::-1]