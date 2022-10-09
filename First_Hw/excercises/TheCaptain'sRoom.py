groups_lenght=int(input())

all_keys=list(map(int,input().split()))

actual_keys=set(all_keys)

cap_rep=len(all_keys)%groups_lenght

for i in range(len(actual_keys)):
    k=actual_keys.pop()
    for j in range(cap_rep):
        all_keys.remove(k)
    if k not in all_keys:
        print(k)
        break
