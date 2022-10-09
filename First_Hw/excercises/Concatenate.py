import numpy
line=list(map(int,input().split()))
mat=[]
for i in range(line[0]+line[1]):
    mat.append(list(map(int,input().split())))
mat=numpy.array(mat)
print(mat)

