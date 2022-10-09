n,colomn=int(input()),input().split()
k=colomn.index("MARKS")
print((sum([int((list(input().split()))[k]) for i in range(n)]))/n)
