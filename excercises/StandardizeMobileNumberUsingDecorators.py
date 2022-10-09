def wrapper(f):
    def fun(l):
        for i in range(len(l)):
            l[i]=("+91 "+l[i][-10:-5]+" "+l[i][-5:])
        
        return(f(l))
    return fun

