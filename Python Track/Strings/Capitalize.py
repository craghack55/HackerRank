#!/bin/python

import sys

def capitalize(string):
    s = string.split(" ")
    temp = []
    
    for word in s:
        word = list(word)
 
        if len(word) != 0:
            word[0] = word[0].upper()
            word = "".join(word)
            temp.append(word)
            temp.append(" ")
        else:
            temp.append(" ")
            
    return "".join(temp)