n=int(input())
mainset=set(map(int,input().split()))
n_othersets=int(input())

for i in range(n_othersets):
    instruction=(input().split())[0]
    otherset=set(map(int,input().split()))
    
    if instruction=="intersection_update":
        mainset.intersection_update(otherset)
    elif instruction=="symmetric_difference_update":
        mainset.symmetric_difference_update(otherset)
    elif instruction=="difference_update":
        mainset.difference_update(otherset)
    elif instruction=="update":
        mainset.update(otherset)
print(sum(mainset))
