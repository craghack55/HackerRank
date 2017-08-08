import itertools
import sys

s = str(raw_input())

groups = itertools.groupby(s)
result = [(label, sum(1 for _ in group)) for label, group in groups]

for i in result:
    sys.stdout.write("(" + str(i[1]) + ", " + str(i[0]) + ") ")