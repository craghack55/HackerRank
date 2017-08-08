#!/bin/python

import sys

def solve(n, p):
    turnedPages = 0
    if  p <= n / 2:
        if p == 1:
            return 0
        else:
            turnedPages = turnedPages + 1
            for i in xrange(2, n / 2 + 1, 2):
                if p == i or p == i + 1:
                    return turnedPages
                else:
                    turnedPages = turnedPages + 1
    else:
        if n % 2 == 0:
            if p == n:
                return 0
            else:
                turnedPages = turnedPages + 1
                for i in xrange(n - 1, n / 2, -2):
                    if p == i or p == i - 1:
                        return turnedPages
                    else:
                        turnedPages = turnedPages + 1

        else:
            if p == n - 1 or p == n:
                return 0
            else:
                turnedPages = turnedPages + 1
                for i in xrange(n - 2, n / 2, -2):
                    if p == i or p == i - 1:
                        return turnedPages
                    else:
                        turnedPages = turnedPages + 1


n = int(raw_input().strip())
p = int(raw_input().strip())
result = solve(n, p)
print(result)