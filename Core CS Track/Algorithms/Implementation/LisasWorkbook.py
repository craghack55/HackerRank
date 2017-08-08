n, k = map(int, raw_input().split(" "))
problems = list(map(int, raw_input().split(" ")))

page = 0
special = 0

for i in problems:
    page += 1
    if i < k:
        if page <= i:
            special += 1
    else:
        for j in range(1, i + 1):
            if j == page:
                special += 1
            
            if j % k == 0 and j != i:
                page += 1
    
    
print special