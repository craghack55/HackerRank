#!/bin/python

import sys    

n,k = raw_input().strip().split(' ')
n,k = [int(n),int(k)]
rQueen,cQueen = raw_input().strip().split(' ')
rQueen,cQueen = [int(rQueen),int(cQueen)]

colUp = n + 1
colDown = 0
rowLeft = 0
rowRight = n + 1

closed = [-1, -1, -1, -1]

# Calculate the squares the queen can attack without obstacles.

freeSquares = 0

# Rows.
freeSquares += n - 1

# Columns.

freeSquares += n - 1

# Diagonals.
freeSquares += n - abs(rQueen - cQueen) - 1
freeSquares += n - abs(n + 1 - (rQueen + cQueen)) - 1

def diagonalCheck(a, flag):
    global freeSquares
    
    if closed[flag] == -1:
        closed[flag] = a
        
        return True
    
    elif closed[flag] < a :
        freeSquares += closed[flag]
        closed[flag] = a
        
        return True
    
    else:
        return False


def ifSameDiagonal(rQueen, cQueen, rObstacle, cObstacle):
    if abs(rQueen - rObstacle) == abs(cQueen - cObstacle):
        if cQueen < cObstacle:
            if rQueen < rObstacle:
                a = min(n - cObstacle + 1, n - rObstacle + 1)
                    
                if diagonalCheck(a, 0):
                    return a
                else:
                    return -1
            else:
                a = min(rObstacle, n - cObstacle + 1)
                
                if diagonalCheck(a, 1):
                    return a
                else:
                     return -1             
        else:
            if rQueen < rObstacle:
                a = min(cObstacle, n - rObstacle + 1)
                
                if diagonalCheck(a, 2):
                    return a
                else:
                    return -1
            else:
                a = min(cObstacle, rObstacle)
                
                if diagonalCheck(a, 3):
                    return a
                else:
                    return -1
                
    else:
        return -1



for a0 in xrange(k):
    rObstacle,cObstacle = raw_input().strip().split(' ')
    rObstacle,cObstacle = [int(rObstacle),int(cObstacle)]
    
    if cObstacle == cQueen:
    # Closed column squares.
        if rObstacle > rQueen :
            if colUp > rObstacle :
                freeSquares -= n - rObstacle + 1
                if colUp != n + 1 : freeSquares += n - colUp + 1
                colUp = rObstacle
        elif colDown < rObstacle :
            freeSquares -= rObstacle
            if colDown != 0 : freeSquares += colDown
            colDown = rObstacle
    elif rObstacle == rQueen:
    # Closed row squares.
        if cObstacle > cQueen :
            if rowRight > cObstacle :
                freeSquares -= n - cObstacle + 1
                if rowRight != n + 1 : freeSquares += n - rowRight + 1
                rowRight = cObstacle
        elif rowLeft < cObstacle :
            freeSquares -= cObstacle
            if rowLeft != 0 : freeSquares += rowLeft
            rowLeft = cObstacle
    else:
        a = ifSameDiagonal(rQueen, cQueen, rObstacle, cObstacle)
        # Closed diagonal sqaures.
        if a != -1:
            freeSquares -= a
            
print freeSquares
    
