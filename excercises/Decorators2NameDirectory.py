

def person_lister(f):
    def inner(people):
        people=sorted(people,key=lambda i:int(i[2]))
        return([f(k) for k in people])
            
    return inner

