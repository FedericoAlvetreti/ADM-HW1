a=[]
for i in range(4):
    a+=[input()]
b=set(a[1].split())
c=set(a[3].split())
d=b.intersection(c)
b=b.difference(d)
c=c.difference(d)
d=list(map(int,b.union(c)))
d.sort()
for i in d:
    print(i)
