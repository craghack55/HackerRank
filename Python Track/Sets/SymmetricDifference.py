M = int(input())
setM = set(map(int, raw_input().split()))
N = int(input())
setN = set(map(int, raw_input().split()))

result = list((setM.union(setN)).difference((setM.intersection(setN))))

for i in sorted(result):
    print i

