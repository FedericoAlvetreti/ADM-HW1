n_eng=int(input())
eng=set(map(int,input().split()))
n_fra=int(input())
fra=set(map(int,input().split()))

not_both=fra.symmetric_difference(eng)

print(len(not_both))
