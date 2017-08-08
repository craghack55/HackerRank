import re

d = "1234567890abcdefABCDEF"
prev = "z"

for i in range(int(raw_input())):
    s = raw_input()
    
    m = re.findall(r"(?<=#)([%s]{3,6})" % d, s)
    
    if m and prev != "}" and prev != "z":
        for i in m:
            if i:
                print "#" + i
    
    if s != "":
        prev = s