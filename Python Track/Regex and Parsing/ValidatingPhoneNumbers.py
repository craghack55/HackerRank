import re

for i in range(int(raw_input())):
    n = raw_input()
    if bool(re.match(r"(7|8|9)(\d){9}$", n)):
        print "YES"
    else:
        print "NO"