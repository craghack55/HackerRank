from collections import Counter

s = Counter(raw_input())
s = s.most_common(3)

for i in sorted(s, key = lambda x: (-x[1], x[0])):
    print str(i[0]) + " " + str(i[1])