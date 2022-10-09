def gain(c_size,s_size):
    money=0
    for i in c_size:
        if i[0] in s_size.keys():
            if s_size[i[0]]!=0:
                money+=i[1]
                s_size[i[0]]-=1
    return(money)




from collections import Counter    


n=int(input())
c_size=[]
s_size=Counter(list(map(int,input().split())))
for i in range(int(input())):
    k=list(map(int,input().split()))
    c_size+=[k]
print(gain(c_size,s_size))
