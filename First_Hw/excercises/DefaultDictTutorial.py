from collections import defaultdict

def list_position(list1):
    dict1=defaultdict(list)
    for i in range(len(list1)):
        dict1[list1[i]].append(i+1)
    return(dict1)

    
indexs=list(map(int,input().split()))
groupA=[]
groupB=[]
for i in range(indexs[0]):
    groupA+=[(input())]
for i in range(indexs[1]): 
    groupB+=[(input())]


for i in groupB:
    if i in groupA:
        k=((list_position(groupA))[i])
        for j in k:
            print(j,end=" ")
        print("")
        
    else:
        print(-1)


