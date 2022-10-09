n_eng=int(input())
eng=set(map(int,input().split()))
n_fra=int(input())
fra=set(map(int,input().split()))

only_eng=eng.difference(fra)

print(len(only_eng))
