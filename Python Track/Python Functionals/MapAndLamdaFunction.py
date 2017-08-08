n = int(raw_input())
temp = []

for i in range(n):
    if i == 0 or i == 1:
        temp.append(i)
    else:
        temp.append(temp[i - 1] + temp[i - 2])
        

print map(lambda x : x**3, temp)
