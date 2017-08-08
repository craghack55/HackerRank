from __future__ import print_function
from collections import OrderedDict

d = OrderedDict()

for _ in range(int(raw_input())):
    word = str(raw_input())
    d[word] = d.get(word, 0) + 1
    
print(len(d))

for w in d.values():
    print(w, end = ' ')
