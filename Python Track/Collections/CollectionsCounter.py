from collections import Counter

x = int(raw_input())
sizes = Counter(map(int, raw_input().split()))
n = int(raw_input())
earned = 0

for i in range(0, n):
    lst = list(map(int, raw_input().split()))
    if sizes.get(lst[0]) > 0:
        earned += lst[1]
        sizes[lst[0]] -= 1
        
print earned