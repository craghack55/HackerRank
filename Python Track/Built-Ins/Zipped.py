n, x = map(int, raw_input().split())

temp = []
for i in range(x):
    grades = list(map(float, raw_input().split()))
    temp.append(grades)
    
for item in zip(*temp):
    print sum(item) / len(item)