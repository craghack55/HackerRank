n = map(int, raw_input())
s = set(map(int, raw_input().split()))
b = map(int, raw_input())
s1 = set(map(int, raw_input().split()))

print len(s.intersection(s1))