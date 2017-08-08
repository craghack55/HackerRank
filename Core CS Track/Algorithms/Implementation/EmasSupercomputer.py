from itertools import combinations
import sys

def getMaxArea(plus):
    if len(plus) == 0:
        return 1
    elif len(plus) == 1:
        return (plus[0][2] - 1) * 4 + 1
    else:
        comb = []
        c = list(combinations(plus, 2))
        
        for i in c:
            if not ifOverlap(i[0], i[1]):
                comb.append(((i[0][2] - 1) * 4 + 1) * ((i[1][2] - 1) * 4 + 1))
        
        if len(comb) == 0:
            l = max(plus, key = lambda x : x[2])
            return (l[2] - 1) * 4 + 1
        else:
            return max(comb)

def ifOverlap(c1, c2):
    
    if c1[0] == c2[0] and c1[1] == c2[1]:
        return True
    else:
        p1 = [[c1[0], c1[1]]]
        p2 = [[c2[0], c2[1]]]
        
        for i in range(1, c1[2]):
            p1.append([c1[0], c1[1] + i])
            p1.append([c1[0], c1[1] - i])
            p1.append([c1[0] + i, c1[1]])
            p1.append([c1[0] - i, c1[1]])
            
            
        for i in range(1, c2[2]):
            p2.append([c2[0], c2[1] + i])
            p2.append([c2[0], c2[1] - i])
            p2.append([c2[0] + i, c2[1]])
            p2.append([c2[0] - i, c2[1]])
            
        for i in p1:
            for j in p2:
                if i[0] == j[0] and i[1] == j[1]:
                    return True
            
        return False
        

n, m = map(int, raw_input().split())

grid = []
plus = []

for i in range(n):
    grid.append(list(raw_input()))
    
for i in range(1, n - 1):
    for j in range(1, m - 1):
        
        if grid[i][j] == "B":
            continue
        else:
            
            limit = min(j, m - j - 1, i, n - i - 1)
            p = 1
            
            for k in range(1, limit + 1):
                if grid[i][j - k] == "B" or grid[i][j + k] == "B" or grid[i - k][j] == "B" or grid[i + k][j] == "B":
                    break
                else:
                    p += 1
                    plus.append([i, j, p])
                
                
print getMaxArea(plus)