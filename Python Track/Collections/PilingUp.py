from collections import deque

d = deque()

for _ in range(int(raw_input())):
    raw_input()
    sideLengths = list(map(int, raw_input().split()))
    top = 0
    
    d.clear()
    
    for i in sideLengths:
        d.append(i)
        
    for i in sideLengths:
        
        if len(d) == 1:
            if d.pop() <= top:
                print "Yes"
                break
            else:
                print "No"
                break
        
        left = d.popleft()
        right = d.pop()
        
        if top != 0:
            if left > top or right > top:
                print "No"
                break
        
        if left >= right:
            top = left
            d.append(right)
        else:
            top = right
            d.appendleft(left)