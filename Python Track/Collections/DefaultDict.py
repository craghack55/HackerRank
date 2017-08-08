from collections import defaultdict

n, m = map(int, raw_input().split())
d = defaultdict(list)

for i in range(0, n):
    word = raw_input()
    d[word].append(str(int(word) + 1))
    
for i in range(0, m):
    word = raw_input()
    print " ".join(s[word]) or -1
    

