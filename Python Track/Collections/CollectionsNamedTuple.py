from collections import namedtuple

n = int(raw_input())
columns = list(map(str, raw_input().split()))
fields = " ".join(columns)
sheet = namedtuple("Grades", fields)
average = 0
for i in range(n):
    temp = list(map(str, raw_input().split()))
    temp = sheet(temp[0], temp[1], temp[2], temp[3])
    average += float(temp.MARKS)
    
print average / n