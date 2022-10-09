def happiness(array,A,B):
    h_level=0
    for i in array:
        if i in A:
            h_level+=1
        if i in B:
            h_level-=1
    return(h_level)

nm=input()
array=list(map(int,input().split()))
A=set(map(int,input().split()))
B=set(map(int,input().split()))
print(happiness(array,A,B))
