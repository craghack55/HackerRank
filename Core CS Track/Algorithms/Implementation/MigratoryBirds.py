#!/bin/python

import sys
from collections import Counter


n = int(raw_input().strip())
types = map(int, raw_input().strip().split(' '))

data = Counter(types)
print data.most_common(1)[0][0]