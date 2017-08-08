import re

def fun(s):   
    result = re.search(r"^[a-zA-Z0-9_-]+@[a-zA-Z0-9]+\.\w{2,3}$", s)
    if result == None:
        return []
    else:
        return result.string
        