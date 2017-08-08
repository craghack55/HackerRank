import numpy as np

result = list(map(float, raw_input().split()))
result = np.array(result)

print np.floor(result)
print np.ceil(result)
print np.rint(result)