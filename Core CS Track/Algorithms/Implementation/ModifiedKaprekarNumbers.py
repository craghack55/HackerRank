from __future__ import print_function

p = int(raw_input())
q = int(raw_input())


def isKaprekar(num):
    temp = num * num
    
    if num == 1:
        return True
    elif len(str(temp)) == 1:
        return False
    
    if len(str(temp)) % 2 == 0:
        r = len(str(temp)) / 2
        l = len(str(temp)) / 2
    else:
        r = len(str(temp)) / 2 + 1
        l = len(str(temp)) / 2
    
    temp = str(temp)
    
    lPiece = int(temp[0:l])
    rPiece = int(temp[l:len(str(temp))])
    
    if rPiece + lPiece == num:
        return True
    else:
        return False

kaprekar = []
for i in range(p, q + 1):
    if isKaprekar(i):
        kaprekar.append(i)
        
if len(kaprekar) == 0:
    print("INVALID RANGE")
else:
    for i in kaprekar:
        print(i, end = " ")