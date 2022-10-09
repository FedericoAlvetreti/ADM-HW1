n_eng=int(input())
eng=set(map(int,input().split()))
n_fra=int(input())
fra=set(map(int,input().split()))

tot_sub=fra.union(eng)

print(len(tot_sub))
