A=set(map(int,input().split()))
n=int(input())
boolean=True
for i in range(n):
    B=set(map(int,input().split()))
    if A.difference(B)=={} or (A!=(A.difference(B).union(B))):
        boolean=False
        break
print(boolean)
