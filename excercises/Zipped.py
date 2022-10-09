k=input().split()
grades=[]
for i in range(int(k[1])):
    grades+=[list(map(float,input().split()))]
grades=zip(*grades)
for i in grades:
    print(sum(i)/int(k[1]))
