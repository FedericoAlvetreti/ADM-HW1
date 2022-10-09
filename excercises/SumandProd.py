import numpy
n=list(map(int,input().split()))[0]
k=[]
for i in range(n):
    k.append(list(map(int,input().split())))
k=numpy.array(k)
print(numpy.prod(numpy.sum(k,axis=0)))
