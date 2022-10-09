def norepeat(parola):
    parola=list(parola)
    new=[]
    for i in parola:
        if i not in new:
            new+=[i]
    new="".join(new)
    return(new)
def merge_the_tools(string, k):
    x=[]
    for i in range(0,len(string),k):
        x+=[string[i:i+k]]
    #lista di sotto parole#
    for i in range(0,len(x)):
        print(norepeat(x[i]))

            
