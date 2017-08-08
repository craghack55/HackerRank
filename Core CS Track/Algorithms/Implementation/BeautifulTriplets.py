n, d = map(int, raw_input().split(" "))
numbers = list(map(int, raw_input().split(" ")))

beautiful = 0

for i in range(n):
    if numbers[i] + d in numbers and numbers[i] + 2 * d in numbers:
        beautiful += 1
        
print beautiful