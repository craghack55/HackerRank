import sys
import itertools

n = int(raw_input())
numbers = list(map(int, raw_input().split()))
maxNumbers = []      

pairs = list(itertools.combinations(numbers, 2))

for pair in pairs:
    if abs(pair[0] - pair[1]) <= 1:
            maxNumbers.append(pair)
            
mergedList = []
multiSets = []

for pair in maxNumbers:
    if not pair[0] in mergedList:
            mergedList.append(pair[0])
        
    if not pair[1] in mergedList:
            mergedList.append(pair[1])
        
 
flag = True

for i in range(2, len(mergedList) + 1):
    multiSet = itertools.combinations(mergedList, i)
    
    if i > 3 and not flag:
        break
    
    for item in multiSet:
        flag = True
        for i in range(0, len(item)):
            if not flag:
                break
            for j in range(i ,len(item)):
                if abs(item[i] - item[j]) > 1:
                    flag = False
                    break
                    
        if flag:
            multiSets.append(item)

temp = []

for i in multiSets:
    counter = 0
    for j in i:
        counter += numbers.count(j)
        
    temp.append(counter)
    
for i in numbers:
    temp.append(numbers.count(i))
    
print max(temp)
