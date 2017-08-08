import sys

def printMatrix(matrix):
    for i in matrix:
        for j in i:
            print(j, end = " ")
            
        print()
    
def rotateMatrix(m, n, r, result, a, layer):
    
    # Find the base case.
    
    outer = 2 * (m - 1) + 2 * (n - 1)
    inner = 2 * (m - 3) + 2 * (n - 3)

    outer = r % outer
    inner = r % inner
    
    rotateMatrix(m - 1, n - 1, inner, result, a, layer + 1)
    
    for i in range(0, n):
        temp = outer
    
        if temp == 0:
            break
    
        if temp <= i:
            result[0][i - temp] = a[0][i]
            result[m - 1][i + temp] = a[m - 1][n - 1 - i]
        else:
            temp -= i
            if temp <= m - 1:
                result[0][temp] = a[0][i]
                result[m - 1 - temp][n - 1] = a[m - 1][n - 1 - i]
            else:
                temp -= m - 1
                if temp <= n - 1:
                    result[m - 1][temp] = a[0][i]
                    result[0][n - 1 - temp] = a[m - 1][n - 1 - i]
                else:
                    temp -= n - 1
                    if temp <= m - 1:
                        result[m - 1 - temp][n - 1] = a[0][i]
                        result[temp][0] = a[m - 1][n - 1 - i]
                    else:
                        temp -= m - 1
                        result[0][n - 1 - temp] = a[0][i]
                        result[m - 1][temp] = a[m - 1][n - 1 - i]

    for i in range(1, m - 1):
        temp = outer
    
        if temp <= m - 1 - i:
            result[i + temp][0] = a[i][0]
            result[m - 1 - i - temp][n - 1] = a[m - 1 - i][n - 1]
        else:
            temp -= m - 1 - i
            if temp <= n - 1:
                result[m - 1][temp] = a[i][0]
                result[0][n - 1 - temp] = a[m - 1 - i][n - 1]
            else:
                temp -= n - 1
                if temp <= m - 1:
                    result[m - 1 - temp][n - 1] = a[i][0]
                    result[temp][0] = a[m - 1 - i][n - 1]
                else:
                    temp -= m - 1
                    if temp <= n - 1:
                        result[0][n - 1 - temp] = a[i][0]
                        result[m - 1][temp] = a[m - 1 - i][n - 1]
                    else:
                        temp -= n - 1
                        result[temp][0] = a[i][0]
                        result[m - 1 - temp][n - 1] = a[m - 1 - i][n - 1]

m, n, r = map(int, input().split())
a = []

for i in range(m):
    a.append(map(int, input().split()))

result = [[0] * m] * n

rotateMatrix(m, n, r, result, a, 0)
printMatrix(result)