import numpy as np
n=list(map(int,input().split()))[0]
k=[]
for i in range(n):
    k.append(list(map(int,input().split())))
k=np.array(k)
print(np.max(np.min(k,axis=1)))
