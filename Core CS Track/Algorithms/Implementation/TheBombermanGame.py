import sys

def printGrid(grid):
    for i in grid:
        print "".join(i)

def getFilledGrid(r ,c):
    g = []
    for i in range(r):
        s = ""
        for j in range(c):
            s += "O"
            
        g.append(list(s))
        
    return g

def printFilledGrid(r ,c):
    g = []
    for i in range(r):
        s = ""
        for j in range(c):
            s += "O"
            
        g.append(s)
        
    printGrid(g)

def getPlanted(grid, r, c):
    p = []
    for i in range(0, r):
        for j in range(0, c):
            if grid[i][j] == "O":
                p.append([i, j])
                
    return p

def detonateBombs(grid, planted, r, c):
    for i in planted:
        row = i[0]
        column = i[1]
        grid[row][column] = "."
        
        if column + 1 != c:
            grid[row][column + 1] = "."
            
        if column != 0:
            grid[row][column - 1] = "."
            
        if row != 0:
            grid[row - 1][column] = "."
            
        if row + 1 != r:
            grid[row + 1][column] = "."
            
    return getPlanted(grid, r, c)

r, c, n = map(int, raw_input().split())

grid = []
gridAfterFirst = []
time = 4

for i in range(r):
    grid.append(list(raw_input()))
    
if n == 1:
    printGrid(grid)
    
elif n % 2 == 0:
    printFilledGrid(r, c)
else:
    planted = getPlanted(grid, r, c)
    
    grid = getFilledGrid(r, c)
    planted = detonateBombs(grid, planted, r, c)
        
    gridAfterFirst = grid
    
    grid = getFilledGrid(r, c)
    planted = detonateBombs(grid, planted, r, c)
        
    if n % 4 == 3:
        printGrid(gridAfterFirst)
    else:
        printGrid(grid)