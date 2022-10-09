import numpy
n=int(input()[0])
mat=[]
for i in range(n):
    mat+=[list(map(int,input().split()))]
mat=numpy.array(mat)
print(numpy.transpose(mat))
print(mat.flatten())
