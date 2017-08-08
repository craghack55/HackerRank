import sys

t = int(raw_input())

for i in range(t):
    n = int(raw_input())
    a = map(int, raw_input().split())
    temp = sorted(a)
    flag = True
    
    for i in range(0, n - 3):
        loc = a.index(temp[i])
        
        while loc != i:
            if loc - i >= 2:
                C = a[loc]
                B = a[loc - 1]
                A = a[loc - 2]
                
                a[loc - 2] = C
                a[loc - 1] = A
                a[loc] = B
                
                loc -= 2
            else:
                C = a[loc + 1]
                B = a[loc]
                A = a[loc - 1]
                
                a[loc + 1] = A
                a[loc] = C
                a[loc - 1] = B
                
                loc -= 1
                
                
    A = a[n - 3]
    B = a[n - 2]
    C = a[n - 1]
    
    if A < B < C or B < C < A or C < A < B:
        print "YES"
    else:
        print "NO"