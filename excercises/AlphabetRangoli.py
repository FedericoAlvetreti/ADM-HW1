az=list(map(chr,range(97,123)))
def print_rangoli(size):
    for i in range(1,2*size):
        v=[]
        j=abs(i-size)
        print(j*"--",end="")
        for k in range(size-1,j-1,-1):
            v+=[az[k]]
        for t in range(j+1,size):
            v+=[az[t]]
        print(v[0],end="")
        for q in range(1,len(v)):
            print("-",v[q],sep="",end="")
        print(j*"--")
