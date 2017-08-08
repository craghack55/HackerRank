from itertools import permutations

s, k = raw_input().split()

p = [x for x in permutations(s, int(k))]

for i in sorted(p):
    print "".join(i)

