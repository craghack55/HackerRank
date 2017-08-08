from collections import Counter

n = int(raw_input())
arr = Counter(map(int, raw_input().split()))

print sum(arr.values()) - max(arr.values())