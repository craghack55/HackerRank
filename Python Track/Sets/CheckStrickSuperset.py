A = set(raw_input().split())
n = int(raw_input())

for i in range(0, n):
    B = set(raw_input().split())
    if len(A.difference(B)) == 0 or len(B.difference(A)) != 0:
        print False
        exit()
    
print True
