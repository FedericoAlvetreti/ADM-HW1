import numpy as np
k=[]
for i in range(list(map(int,input().split()))[0]):
    k.append(list(map(int,input().split())))
k=np.array(k)
print(np.mean(k,axis=1),np.var(k,axis=0),round(np.std(k),11),sep="\n")
