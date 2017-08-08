n = int(raw_input())

liked = 0
people = 5

for i in range(n):
    liked += people / 2
    people = people / 2 * 3
    
    
print liked