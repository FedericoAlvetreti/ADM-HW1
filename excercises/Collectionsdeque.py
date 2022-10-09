from collections import deque

n=int(input())
result=deque()
for i in range(n):
    k=input().split()
    if k[0]=="append":
        result.append(int(k[1]))
    elif k[0]=="appendleft":
        result.appendleft(int(k[1]))
    elif k[0]=="pop":
        result.pop()
    elif k[0]=="popleft":
        result.popleft()
for i in result:
    print(i,end=" ")
