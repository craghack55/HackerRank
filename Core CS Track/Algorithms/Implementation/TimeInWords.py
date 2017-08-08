#!/bin/python

import sys


h = int(raw_input().strip())
m = int(raw_input().strip())

d = {"1" : "one", "2" : "two", "3" : "three", "4" : "four", "5" : "five", "6" : "six", "7" : "seven", "8" : "eight", "9" : "nine", "10" : "ten", "11" : "eleven", "12" : "twelve", "13" : "thirteen", "14" : "fourteen", "15" : "fifteen", "16" : "sixteen", "17" : "seventeen", "18" : "eighteen", "19" : "nineteen", "20" : "twenty", "30" : "thirty", "40" : "fourty", "50" : "fifty"}

def constructTime(time):
    strTime = str(time)
    
    if len(strTime) == 1 or (len(strTime) == 2 and time <= 12):
        return d[strTime]
    elif time > 20:
        return d[str(int(strTime[0]) * 10)] + " " + d[strTime[1]]
    else:
        return d[strTime]

if m == 0:
    print constructTime(h) + " o' clock"
elif m == 15:
    print "quarter past " + constructTime(h)
elif m < 30:
    print constructTime(m) + " minutes past " + constructTime(h)
elif m == 30:
    print "half past " + constructTime(h)
elif m == 45:
    print "quarter to " + constructTime(h + 1)
else:
    print constructTime(60 - m) + " minutes to " + constructTime(h + 1)
    