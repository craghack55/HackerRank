import re

def change(match):
    sym = match.group(0)
    print "sdfsdf"
    print sym

n, m = map(int, raw_input().split())
a, b = [], ""

for _ in range(n):
    a.append(raw_input())

for z in zip(*a):
    b += "".join(z)
    
print re.sub(r"(?<=\w)(\W)(?=\w)", change, b)
