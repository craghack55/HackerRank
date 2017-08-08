import numpy as np

a = list(map(int, raw_input().split()))
a = np.array(a)
a.shape = (3, 3)

print a