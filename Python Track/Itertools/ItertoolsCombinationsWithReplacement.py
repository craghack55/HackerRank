from itertools import combinations_with_replacement

s, k = raw_input().split()

p = [x for x in combinations_with_replacement(sorted(s), int(k))]

for i in sorted(p):
    print "".join(i)