from collections import OrderedDict

d = OrderedDict()

for _ in range(int(raw_input())):
    item, space, quantity = raw_input().rpartition(' ')
    d[item] = d.get(item, 0) + int(quantity)
    
for item, quantity in d.items():
    print item, quantity