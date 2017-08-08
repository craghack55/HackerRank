n = raw_input()
s = set(map(int, raw_input().split()))
c = raw_input()

for i in range(0, int(c)):
    com = map(str, raw_input().split())
    
    if com[0] == "pop":
        s.pop()
    elif com[0] == "remove":
        if int(com[1]) in s:
            s.remove(int(com[1]))
    elif com[0] == "discard":
        s.discard(int(com[1]))
        

print sum(s)


