def wrapper(f):
    def fun(l):
        temp = []
        for i in list(l):
            if i[0] == "+" and len(i) != 10:
                temp.append("+91 " + i[3:8] + " " + i[-5:])
            elif i[0] == "9" and len(i) != 10:
                temp.append("+91 " + i[2:7] + " " + i[-5:])
            elif i[0] == "0" and len(i) != 10:
                temp.append("+91 " + i[1:6] + " " + i[-5:])
            else:
                temp.append("+91 " + i[:5] + " " + i[-5:])
    
        f(temp)
    
    return fun