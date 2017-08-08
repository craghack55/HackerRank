N, M = map(int, raw_input().split())
arr = list(map(int, raw_input().split()))
setM = set(map(int, raw_input().split()))
setN = set(map(int, raw_input().split()))
happiness = 0

for i in arr:
    if i in setM:
        happiness += 1
    elif i in setN:
        happiness -= 1
        
print happiness