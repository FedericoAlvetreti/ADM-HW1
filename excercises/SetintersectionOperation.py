n_eng=int(input())
eng=set(map(int,input().split()))
n_fra=int(input())
fra=set(map(int,input().split()))

both_sub=fra.intersection(eng)

print(len(both_sub))
