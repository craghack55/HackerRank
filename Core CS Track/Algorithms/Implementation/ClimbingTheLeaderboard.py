from bisect import bisect_left

n = int(raw_input().strip())
scores = map(int,raw_input().strip().split(' '))
m = int(raw_input().strip())
alice = map(int,raw_input().strip().split(' '))


scores = sorted(list(set(scores)))
l = len(scores)

prev = 0

for score in alice:
    p = bisect_left(scores, score, prev)
    
    if p != l and scores[p] == score:
        print l - p
    else:
        print l - p + 1

    prev = p