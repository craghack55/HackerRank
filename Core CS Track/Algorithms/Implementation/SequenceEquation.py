n = int(raw_input())
a = map(int,raw_input().strip().split(' '))

for i in range(1, n + 1):
    idx = a.index(i) + 1
    print a.index(idx) + 1