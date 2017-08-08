import re

for i in range(int(raw_input())):
    uid = raw_input()
    
    if bool(re.search(r"([A-Z].*){2}", uid)) and bool(re.search(r"([0-9].*){3}", uid)) and bool(re.search(r"^[a-zA-Z0-9]{10}$", uid)) and not bool(re.search(r"([a-zA-Z0-9]).*\1", uid)):
        print "Valid"
    else:
        print "Invalid"