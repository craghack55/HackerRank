from datetime import datetime
from dateutil.parser import parse

t = int(input())

for i in range(t):
    d1 = parse(input())
    d2 = parse(input())
    
    print(int(abs((d1 - d2).total_seconds())))