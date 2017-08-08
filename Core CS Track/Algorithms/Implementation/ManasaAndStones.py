from __future__ import print_function

T = int(raw_input())

for i in range(T):
    n = int(raw_input())
    a = int(raw_input())
    b = int(raw_input())
    
    stones = []
    
    if a != b:
        for i in range(0, n):
            stones.append(i * a + (n - i - 1) * b)
    else:
        stones.append(a * (n - 1))
    
    for i in sorted(stones):
        print(i, end = " ")
        
    if i != T - 1:
        print()