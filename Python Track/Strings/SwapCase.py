#!/bin/python

import sys

def swap_case(s):
    result = list(s)
    for i in range (0, len(result)):
        if result[i].isupper():
            result[i] = str(result[i]).lower()
        else:
            result[i] = result[i].upper()
            
    return ''.join(result)