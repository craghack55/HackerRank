import re

t = int(raw_input())

for i in range(t):
    r = raw_input()
    try:
        re.compile(r)
        print True
    except re.error as e:
        print False
    
