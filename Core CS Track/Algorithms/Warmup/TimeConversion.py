import sys


time = raw_input().strip()

t = map(str, time.split(':'))

if "PM" in t[-1]:
    if int(t[0]) != 12:
        t[0] = str(int(t[0]) + 12)
else:
    if int(t[0]) == 12:
        t[0] = "00"
        
t[-1] = t[-1][:-2]
result = t[0]
        
for i in range(1, len(t)):
    result = result + ":" + t[i]
    
print result