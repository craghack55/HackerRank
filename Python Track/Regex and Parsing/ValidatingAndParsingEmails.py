import email.utils
import re

for i in range(int(raw_input())):
    s = email.utils.parseaddr(raw_input())
    
    if bool(re.search("^[a-zA-Z][a-zA-Z0-9_-\.]+@[a-zA-Z]+\.[a-zA-Z]{1,3}$", s[1])):
        print s[0] + " " + "<" + s[1] + ">"