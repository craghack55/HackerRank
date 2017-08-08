import math

n = int(raw_input())

for i in range(n):
    x, y = map(int, raw_input().split())
    
    print int(math.floor(math.sqrt(y)) - math.ceil(math.sqrt(x)) + 1)
    