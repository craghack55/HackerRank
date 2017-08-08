#!/bin/python

import sys

def solve(year):
    month = ""
    day = ""
    if year <= 1917:
        month = "09"
        if year % 4 == 0:
            day = "12"
        else:
            day = "13"
    elif year != 1918:
        month = "09"
        if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
            day = "12"
        else:
            day = "13"
    else:
        month = "09"
        day = "26"
        
        
    return day + "." + month + "." + str(year)

year = int(raw_input().strip())
result = solve(year)
print(result)
