import numpy

a=[]
b=[]
dim=list(map(int,input().split()))
for i in range(dim[0]):
    a.append(list(map(int,input().split())))

for i in range(dim[0]):
    b.append(list(map(int,input().split())))
a=numpy.array(a)
b=numpy.array(b)
print(a+b,a-b,a*b,a//b,a%b,a**b,sep="\n")
