N = int(raw_input())
stamps = set()

for i in range(0, N):
    country = str(raw_input())
    stamps.add(country)
    
print len(stamps)