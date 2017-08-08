#!/bin/python

import sys

def minion_game(string):

    v = ['A', 'E', 'I', 'O', 'U']
    Kevin = 0
    Stuart = 0
    
    for i in range(0, len(s)):
        if s[i] in v:
            Kevin += len(s) - i
        else:
            Stuart += len(s) - i 
    
    if Stuart > Kevin:
        print "Stuart" + " " + str(Stuart)
    elif Kevin > Stuart:
        print "Kevin" + " " + str(Kevin)
    else:
        print "Draw"