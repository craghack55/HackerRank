import re

for i in range(int(raw_input())):
    uid = raw_input()
    
    if bool(re.search(r"^[456]", uid)) and not bool(re.search(r"[,_\s]", uid)) and (bool(re.match(r"(\d{4}-){3}\d{4}$", uid)) or bool(re.match(r"[0-9]{16}$", uid))) and not bool(re.search(r"(.)(-?\1){3}", uid)):
        print "Valid"
    else:
        print "Invalid"