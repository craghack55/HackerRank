n = int(raw_input())
s = list(map(int, raw_input().split()))

rooms = set(s)

print abs(sum(s) - sum([x * n for x in rooms])) / (n - 1)