cases=int(input())

for i in range(cases):
    nA=int(input())
    A=set(map(int,input().split()))
    nB=int(input())
    B=set(map(int,input().split()))
    
    
    if B==(B.difference(A)).union(A):
        print(True)
    else:
        print(False)
