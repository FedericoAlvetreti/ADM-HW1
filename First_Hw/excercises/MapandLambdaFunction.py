cube = lambda x:x**3

def fibonacci(n):
    if n==0:
        return([])
    if n==1:
        return([0])
    lista=[0,1]
    for i in range(n-2):
        lista.append(sum(lista[-2:]))
    return(lista)

