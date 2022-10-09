if __name__ == '__main__':
    a={}
    k=0
    nomi=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        a[name]=score
    valori=list(a.values())
    valori.sort()
    for i in valori:
        if i!=valori[0]:
            k=i
            break
    for i in list(a.keys()):
        if a[i]==k:
            nomi+=[i]
    nomi.sort()
    for i in nomi:
        print(i,end="\n")
   

