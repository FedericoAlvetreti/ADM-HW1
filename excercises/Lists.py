if __name__ == '__main__':
    N = int(input())
    Comando=""
    x=[]
    for i in range(0,N):
        Comando=input()
        y=Comando.split(" ")
        
        if y[0]=="insert":
            x.insert(int(y[1]),int(y[2]))
        elif y[0]=="print":
            print(x)
        elif y[0]=="remove":
            x.remove(int(y[1]))
        elif y[0]=="append":
            x.append(int(y[1]))
        elif y[0]=="sort":
            x.sort()
        elif y[0]=="pop":
            x.pop()
        elif y[0]=="reverse":
            x.reverse()
    
