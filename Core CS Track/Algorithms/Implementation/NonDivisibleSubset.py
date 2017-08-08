from collections import Counter
import itertools

n, k = map(int, raw_input().strip().split(' '))
arr = map(int, raw_input().strip().split(' '))        

remainders = Counter([x % k for x in arr])

result = 0

for i in range(0, k / 2 + 1):
    if i in remainders.keys():
        if i == 0 or (k % 2 == 0 and i == k / 2):
            result += 1
        else:
            if remainders.get(i) >= remainders.get(k - i):
                result += remainders.get(i)
            else:
                result += remainders.get(k - i)
    else:
        if k - i in remainders.keys():
            result += remainders.get(k - i)


print result

        
            