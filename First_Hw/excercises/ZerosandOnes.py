import numpy
dim=list(map(int,input().split()))
dim=tuple(dim)
print(numpy.zeros(dim,dtype=numpy.int))
print(numpy.ones(dim,dtype=numpy.int))
