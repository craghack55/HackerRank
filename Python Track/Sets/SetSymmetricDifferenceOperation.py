n = map(int, raw_input().split())
s = set(map(int, raw_input().split()))
b = map(int, raw_input().split())
s1 = set(map(int, raw_input().split()))

print len((s.union(s1)).difference(s.intersection(s1)))
