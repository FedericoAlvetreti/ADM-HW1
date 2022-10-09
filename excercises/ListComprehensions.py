if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    a=[]
    for i in range(0,x+1):
        for j in range(0,y+1):
            for k in range(0,z+1):
                a+=[[i,j,k]]
    b=[t for t in a if (t[0]+t[1]+t[2])!=n]
    print(b)
   
