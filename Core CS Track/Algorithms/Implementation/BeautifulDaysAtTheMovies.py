i, j, k = raw_input().strip().split(' ')
i, j, k = [int(i), int(j), int(k)]

beautiful = 0


def getReverse(number):
    temp = str(number)
    return int(temp[::-1])

for z in range(i, j + 1):
    if abs(z - getReverse(z)) % k == 0:
        beautiful += 1
        
print beautiful
