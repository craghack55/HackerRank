from itertools import combinations

s, k = raw_input().split()


for i in range(1, int(k) + 1):

    p = [x for x in combinations(sorted(s), i)]

    for i in sorted(p):
        print "".join(i)
