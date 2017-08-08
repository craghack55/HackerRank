import re

n = int(raw_input())

for i in range(n):
    s = str(raw_input())
    
    if bool(re.match(r'[+-]?\d*\.\d+$', s)):
        print True
    else:
        print False

