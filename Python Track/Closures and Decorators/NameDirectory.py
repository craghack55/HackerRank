def person_lister(f):
    def inner(people):
        temp = []
        
        for person in sorted(people, key = lambda x : x[2]):
            temp.append(f(person))
            
        return temp
    
    return inner