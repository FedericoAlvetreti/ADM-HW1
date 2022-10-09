if __name__ == '__main__':
    s = input()
    a=False
    b=False
    c=False
    d=False
    e=False
    for i in s:
        if i.isalnum()==True and a==False:
            a=True
        if i.isalpha()==True and b==False:
            b=True
        if i.isdigit()==True and c==False:
            c=True
        if i.islower()==True and d==False:
            d=True
        if i.isupper()==True and e==False:
            e=True
    print(a,b,c,d,e,sep="\n")
