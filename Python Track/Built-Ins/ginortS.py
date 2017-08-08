from __future__ import print_function

s = raw_input()

print(*sorted(s, key = lambda c : (c.isdigit() and int(c) % 2 == 0, c.isdigit() and int(c) % 2 != 0, c.isupper(), c.islower(), c)), sep = "")