from collections import deque



def cubable(vet):
    result=[]
    vet=deque(vet)
    for i in range(len(vet)):
        if vet[0]>vet[-1]:
            result+=[vet.popleft()]
        else:
            result+=[vet.pop()]
    return(result==sorted(result,reverse=True))



t=int(input())
for i in range(t):
    n=int(input())
    vet=list(map(int,input().split()))
    if cubable(vet)==True:
        print("Yes")
    else:
        print("No")
