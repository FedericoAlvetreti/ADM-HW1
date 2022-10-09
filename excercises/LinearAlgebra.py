import numpy
k=[]
for i in range(int(input())):
    k.append(list(map(float,input().split())))
print(round(numpy.linalg.det(k),2))
