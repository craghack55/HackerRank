import numpy as np

P = list(map(float, raw_input().split()))
x = float(raw_input())

print np.polyval(P, x)
