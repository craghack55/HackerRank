import re

s = str(raw_input())
k = str(raw_input())

m = re.finditer(r"(?=(%s))" % k, s)
result =  "\n".join([(i.start(1), i.end(1) - 1) for i in m])

if result == "":
    print "(-1, -1)"
else:
    print result