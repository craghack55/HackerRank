import re

def changeAndOr(match):
    sym = match.group(0)
    
    if sym == "&&":
        return "and"
    else:
        return "or"


for i in range(int(raw_input())):
    line = raw_input()
    print re.sub(r"(?<= )(&&|\|\|)(?= )", changeAndOr, line)
    
    