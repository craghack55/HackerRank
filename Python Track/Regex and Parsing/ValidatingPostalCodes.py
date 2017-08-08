import re

"""pc = raw_input()
flag = bool(int(pc) => 100000 and int(pc) <= 999999)
temp = True

for i in range(0, len(pc) - 2):
    temp += bool(pc[i] == pc[i + 2])

print flag and bool(temp == 1 or temp == 2)"""

import re

P = raw_input()

print(P.isdigit() and 100000 <= int(P) <= 999999 and bool(re.match(r'(((\d\d)(?!\3)){3})', P)))