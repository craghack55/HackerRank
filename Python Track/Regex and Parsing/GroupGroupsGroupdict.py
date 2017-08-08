from __future__ import print_function
import re

s = str(raw_input())

m = re.search(r'([a-zA-Z\d])\1', s)

print(m.group(1) if m else -1)